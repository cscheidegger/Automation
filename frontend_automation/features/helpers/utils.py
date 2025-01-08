from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def wait_and_click(driver, locator):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
        logging.info(f"Clicked on element: {locator}")
    except Exception as e:
        logging.error(f"Error clicking element {locator}: {e}")
        raise

def wait_and_send_keys(driver, locator, keys):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(keys)
        logging.info(f"Sent keys '{keys}' to element: {locator}")
    except Exception as e:
        logging.error(f"Error sending keys to element {locator}: {e}")
        raise
