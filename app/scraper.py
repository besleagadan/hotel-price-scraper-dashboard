import time
from datetime import date
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from db.connect import get_connection
from db.mixins import validate_hotel
from app.logger import logger
from app.utils import (
    wait_for_element,
    wait_for_element_clickable,
    click_js,
    clean_price
)


def get_driver(headless=True):
    """
    Returns a Chrome driver instance.

    Args:
        headless (bool): Run in headless mode if True. GUI mode if False.

    Returns:
        undetected_chromedriver.Chrome: Chrome WebDriver instance.
    """
    options = Options()

    # Headless mode is more stable for automation
    if headless:
        options.add_argument("--headless=new")

    # Common stability flags for macOS
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Optional: remote debugging keeps window alive in GUI mode
    if not headless:
        options.add_argument("--remote-debugging-port=9222")

    # Set window size for GUI to avoid zero-size errors
    options.add_argument("--window-size=1920,1080")

    # Create driver
    driver = uc.Chrome(options=options)

    # Optional: add a small wait after startup
    driver.implicitly_wait(2)

    return driver


def scrape_booking(location="Paris", checkin="2025-09-01", checkout="2025-09-02"):
    driver = get_driver(headless=False)
    url = (
        f"https://www.booking.com/searchresults.html?"
        f"ss={location}&checkin_year_month_monthday={checkin}"
        f"&checkout_year_month_monthday={checkout}"
    )
    driver.get(url)

    time.sleep(2)

    # Close check-in modal
    dates_button = wait_for_element_clickable(driver, By.CSS_SELECTOR, "button[data-testid='searchbox-dates-container']")
    click_js(driver, dates_button)

    # Open sort dropdown and select "Price from high to low"
    sort_button = wait_for_element_clickable(driver, By.CSS_SELECTOR, "button[data-testid='sorters-dropdown-trigger']")
    click_js(driver, sort_button)

    option = wait_for_element_clickable(driver, By.CSS_SELECTOR, "button[data-id='price_from_high_to_low']")
    click_js(driver, option)

    results = wait_for_element(driver, By.CSS_SELECTOR, "div[data-testid='property-card']")

    hotels = []
    for hotel_card in results[:10]:
        hotels.append(get_hotel_info(hotel_card))

    driver.quit()
    return hotels

def get_hotel_info(hotel_card):
    name = "N/A"
    price = "N/A"
    try:
        name = hotel_card.find_element(By.CSS_SELECTOR, "div[data-testid='title']").text
        price = hotel_card.find_element(By.CSS_SELECTOR, "span[data-testid='price-and-discounted-price']").text
    except Exception as e:
        logger.error("Error", e)

    return {"name": name, "price": price, "source": "Booking.com"}


def save_hotels(hotels, location):
    """Save a list of hotels to the database."""
    if not hotels:
        return

    # use `with` for automatic cleanup
    with get_connection() as conn:
        with conn.cursor() as cur:
            for hotel in hotels:
                if validate_hotel(hotel):
                    continue

                price = clean_price(hotel.get("price"))
                if not price:
                    continue

                cur.execute(
                    """
                    INSERT INTO hotels (name, location, date, price, source)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (name, location, date, source) DO UPDATE
                    SET price = EXCLUDED.price
                    """,
                    (hotel.get("name"), location, date.today(), price, hotel.get("source"))
                )
        conn.commit()


if __name__ == "__main__":
    flights = scrape_booking()
    print(flights)

