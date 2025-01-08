import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    """Base class for common WebDriver interactions."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def validate_window(self):
        """Ensure WebDriver is aware of open windows."""
        if not self.driver.window_handles:
            raise Exception("No browser windows are currently open.")

    def navigate(self, url):
        """Navigate to a specific URL."""
        try:
            logging.info(f"Navigating to URL: {url}")
            self.driver.get(url)
        except Exception as e:
            logging.error(f"Error navigating to URL {url}: {e}")
            raise

    def click(self, locator, retries=3):
        """Wait for an element to be clickable and then click it."""
        for attempt in range(retries):
            try:
                logging.info(f"Attempting to click element: {locator}")
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                logging.info(f"Clicked element: {locator}")
                return
            except StaleElementReferenceException as stale_err:
                logging.warning(f"Stale element reference on attempt {attempt + 1} for {locator}: {stale_err}")
                if attempt == retries - 1:
                    raise
            except Exception as e:
                logging.error(f"Error clicking element {locator}: {e}")
                raise

    def send_keys(self, locator, text, retries=3):
        """Wait for an element to be present and send keys."""
        for attempt in range(retries):
            try:
                logging.info(f"Sending keys to element: {locator}")
                element = self.wait.until(EC.presence_of_element_located(locator))
                element.clear()  # Clear the field before typing
                element.send_keys(text)
                logging.info(f"Sent keys to element: {locator}")
                return
            except StaleElementReferenceException as stale_err:
                logging.warning(f"Stale element reference on attempt {attempt + 1} for {locator}: {stale_err}")
                if attempt == retries - 1:
                    raise
            except Exception as e:
                logging.error(f"Error sending keys to element {locator}: {e}")
                raise

    def get_text(self, locator):
        """Get the text of a specific element."""
        try:
            logging.info(f"Getting text from element: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            text = element.text
            logging.info(f"Text retrieved from element {locator}: {text}")
            return text
        except Exception as e:
            logging.error(f"Error getting text from element {locator}: {e}")
            raise

    def is_element_visible(self, locator, timeout=10):
        """Check if an element is visible on the page within a given timeout."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            logging.info(f"Checking visibility of element: {locator}")
            wait.until(EC.visibility_of_element_located(locator))
            logging.info(f"Element is visible: {locator}")
            return True
        except Exception as e:
            logging.info(f"Element is not visible: {locator}, Error: {e}")
            return False

    def scroll_to_element(self, locator):
        """Scroll the page to bring an element into view."""
        try:
            logging.info(f"Scrolling to element: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logging.info(f"Scrolled to element: {locator}")
        except Exception as e:
            logging.error(f"Error scrolling to element {locator}: {e}")
            raise

    def execute_script(self, script, *args):
        """Execute custom JavaScript on the page."""
        try:
            logging.info(f"Executing script: {script}")
            result = self.driver.execute_script(script, *args)
            logging.info(f"Script executed successfully: {script}")
            return result
        except Exception as e:
            logging.error(f"Error executing script: {script}, Error: {e}")
            raise

    def switch_to_main_window(self):
        """Switch to the main browser window."""
        try:
            main_window = self.driver.window_handles[0]
            self.driver.switch_to.window(main_window)
            logging.info(f"Switched to the main window: {main_window}")
        except Exception as e:
            logging.error(f"Error switching to main window: {e}")
            raise
