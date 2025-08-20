from app.logger import logger
from app.scraper import scrape_booking, save_hotels


if __name__ == "__main__":
    hotels = scrape_booking("Paris")
    logger.info("Scraped:", hotels)
    save_hotels(hotels, "Paris")
    logger.info("✅ Data saved to database")
