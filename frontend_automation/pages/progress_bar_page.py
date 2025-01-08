from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import logging
import time

class ProgressBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/progress-bar"
        self.locators = {
            "progress_bar_button": (By.XPATH, "//span[text()='Progress Bar']"),
            "start_stop_button": (By.ID, "startStopButton"),
            "progress_bar": (By.CSS_SELECTOR, ".progress-bar"),
            "fixed_banner": (By.ID, "fixedban"),  # Locator for the interfering banner
            "footer": (By.TAG_NAME, "footer"),   # Locator for the interfering footer
        }

    def navigate_to_progress_bar(self):
        self.navigate(self.url)
        self.remove_fixed_banner()  # Ensure the banner is removed before clicking
        self.remove_footer()        # Ensure the footer is removed before clicking
        self.click(self.locators["progress_bar_button"])
        logging.info("Opened Progress Bar page.")

    def remove_fixed_banner(self):
        """Remove or hide the fixed banner to prevent click interception."""
        try:
            banner = self.driver.find_element(*self.locators["fixed_banner"])
            self.driver.execute_script("arguments[0].style.display = 'none';", banner)
            logging.info("Fixed banner removed to prevent click interception.")
        except Exception as e:
            logging.warning(f"Fixed banner not found or could not be removed: {e}")

    def remove_footer(self):
        """Remove or hide the footer to prevent click interception."""
        try:
            footer = self.driver.find_element(*self.locators["footer"])
            self.driver.execute_script("arguments[0].style.display = 'none';", footer)
            logging.info("Footer removed to prevent click interception.")
        except Exception as e:
            logging.warning(f"Footer not found or could not be removed: {e}")

    def click_start_button(self):
        self.click(self.locators["start_stop_button"])
        logging.info("Clicked Start/Stop button.")

    def wait_for_progress(self, target_percentage=24, timeout=30):
        try:
            while True:
                current_value = int(self.driver.find_element(*self.locators["progress_bar"]).get_attribute("aria-valuenow"))
                if current_value >= target_percentage - 1:
                    self.click(self.locators["start_stop_button"])
                    logging.info(f"Stopped progress bar at {current_value}%")
                    break
                time.sleep(0.1)
        except Exception as e:
            logging.error(f"Error waiting for progress: {e}")
            raise

    def get_progress_value(self):
        progress_element = self.driver.find_element(*self.locators["progress_bar"])
        return int(progress_element.get_attribute("aria-valuenow"))

    def reset_progress_bar(self):
        self.click(self.locators["start_stop_button"])
        logging.info("Reset progress bar.")
