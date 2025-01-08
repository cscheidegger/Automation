from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)

def validate_locators():
    driver = webdriver.Chrome()  # Change to your preferred WebDriver
    driver.get("https://demoqa.com/webtables")  # Open the Web Tables page

    try:
        # Validate Add New Record Button
        try:
            add_record_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "addNewRecordButton"))
            )
            logging.info("Add Record Button Found: PASS")
        except Exception as e:
            logging.error(f"Add Record Button Found: FAIL - {e}")

        # Validate Edit Button
        try:
            edit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[id^='edit-record-']"))
            )
            logging.info("Edit Button Found: PASS")
        except Exception as e:
            logging.error(f"Edit Button Found: FAIL - {e}")

        # Validate Delete Button
        try:
            delete_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[id^='delete-record-']"))
            )
            logging.info("Delete Button Found: PASS")
        except Exception as e:
            logging.error(f"Delete Button Found: FAIL - {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    validate_locators()
