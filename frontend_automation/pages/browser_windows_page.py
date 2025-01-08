from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import logging


class BrowserWindowsPage(BasePage):
    """Page object for the Browser Windows page."""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/browser-windows"
        self._init_locators()
        self.main_window = None

    def _init_locators(self):
        """Initialize all locators for the browser windows page."""
        self.locators = {
            "browser_windows_button": (By.CSS_SELECTOR, "#item-0"),
            "new_window_button": (By.ID, "windowButton"),
            "sample_heading": (By.ID, "sampleHeading"),
            "body_content": (By.TAG_NAME, "body")
        }

    def open(self):
        """Open the Browser Windows page."""
        self.navigate(self.url)
        self.main_window = self.driver.current_window_handle
        # Remove fixed banner and hide iframes
        self.driver.execute_script("""
            // Remove fixedban
            var banner = document.getElementById('fixedban');
            if(banner) banner.remove();
            
            // Hide iframes
            document.querySelectorAll('iframe').forEach(iframe => iframe.style.display = 'none');
        """)
        logging.info(f"Opened Browser Windows page. Main window handle: {self.main_window}")

    def click_browser_windows_button(self):
        """Click the 'Browser Windows' button."""
        self.click(self.locators["browser_windows_button"])
        logging.info("Clicked Browser Windows button")

    def click_new_window(self):
        """Click the 'New Window' button."""
        try:
            # Remove fixed banner and hide iframes
            self.driver.execute_script("""
                // Remove fixedban
                var banner = document.getElementById('fixedban');
                if(banner) banner.remove();
                
                // Hide iframes
                document.querySelectorAll('iframe').forEach(iframe => iframe.style.display = 'none');
            """)
            logging.info("Hidden iframes and removed banner to prevent click interception.")
            
            # Use JavaScript click for better reliability
            button = self.driver.find_element(*self.locators["new_window_button"])
            self.driver.execute_script("arguments[0].click();", button)
            logging.info("Clicked New Window button")
        except Exception as e:
            logging.error(f"Error clicking new window button: {e}")
            raise

    def switch_to_new_window(self, timeout=10):
        """Switch to the newly opened window/tab."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: len(driver.window_handles) > 1
            )
            all_handles = self.driver.window_handles
            new_handle = [handle for handle in all_handles if handle != self.main_window][0]
            self.driver.switch_to.window(new_handle)
            logging.info(f"Switched to new window: {new_handle}")
            return new_handle
        except Exception as e:
            logging.error(f"Error switching to new window: {e}")
            raise

    def get_new_window_text(self):
        """Get the text content from the new window."""
        try:
            # Wait for new window and switch to it
            WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
            new_window = [handle for handle in self.driver.window_handles 
                         if handle != self.main_window][0]
            self.driver.switch_to.window(new_window)
            
            # Wait for and get text
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "sampleHeading"))
            )
            return element.text
        except Exception as e:
            logging.error(f"Error getting text from new window: {e}")
            raise

    def close_new_window_and_switch_back(self):
        """Close the current window and switch back to the main window."""
        try:
            current_window = self.driver.current_window_handle
            logging.info(f"Closing current window: {current_window}")
            self.driver.close()
            self.driver.switch_to.window(self.main_window)
            logging.info(f"Switched back to main window: {self.main_window}")
        except Exception as e:
            logging.error(f"Error closing window and switching back: {e}")
            raise

    def handle_window_interaction(self, expected_text=None):
        """
        Handle the complete window interaction flow.

        Args:
            expected_text (str): Expected text to verify in the new window
        """
        try:
            self.click_new_window()
            new_window = self.switch_to_new_window()
            logging.info(f"Interacting with new window: {new_window}")

            if expected_text:
                actual_text = self.get_new_window_text()
                assert expected_text in actual_text, f"Expected text '{expected_text}' not found in window"

            self.close_new_window_and_switch_back()
            logging.info("Successfully completed window interaction")
        except Exception as e:
            logging.error(f"Error in window interaction: {e}")
            raise