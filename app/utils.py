import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_js(driver, element):
    driver.execute_script("arguments[0].click();", element)


def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_all_elements_located((by, value))
    )


def wait_for_element_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )


def clean_price(price_str):
    digits = re.findall(r"\d+", price_str.replace(",", ""))
    return float("".join(digits)) if digits else None
