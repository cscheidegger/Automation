from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import logging
import time


class WebTablesPage(BasePage):
    """Page Object for Web Tables functionality."""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/elements"
        self.locators = {
            "web_tables_button": (By.XPATH, "//span[text()='Web Tables']"),
            "add_button": (By.ID, "addNewRecordButton"),
            "first_name": (By.ID, "firstName"),
            "last_name": (By.ID, "lastName"),
            "email": (By.ID, "userEmail"),
            "age": (By.ID, "age"),
            "salary": (By.ID, "salary"),
            "department": (By.ID, "department"),
            "submit_button": (By.ID, "submit"),
            "edit_buttons": (By.CSS_SELECTOR, "span[title='Edit']"),
            "delete_buttons": (By.CSS_SELECTOR, "span[title='Delete']"),
            "table_rows": (By.CSS_SELECTOR, ".rt-tr-group"),
        }

    def navigate_to_web_tables(self):
        """Navigate to the Web Tables page through Elements."""
        self.navigate(self.url)
        logging.info("Navigated to Elements page.")

        # Hide iframes to avoid click interception
        self.driver.execute_script(
            "document.querySelectorAll('iframe').forEach(iframe => iframe.style.display = 'none');"
        )
        logging.info("Hidden iframes to prevent click interception.")

        self.click(self.locators["web_tables_button"])
        logging.info("Opened Web Tables page.")

    def add_new_record(self, data):
        """Add a new record to the table."""
        self.click(self.locators["add_button"])
        logging.info("Clicked 'Add' button.")

        self.send_keys(self.locators["first_name"], data["first_name"])
        self.send_keys(self.locators["last_name"], data["last_name"])
        self.send_keys(self.locators["email"], data["email"])
        self.send_keys(self.locators["age"], str(data["age"]))
        self.send_keys(self.locators["salary"], str(data["salary"]))
        self.send_keys(self.locators["department"], data["department"])

        self.click(self.locators["submit_button"])
        logging.info(f"Added new record: {data}.")

    def edit_last_record(self, updated_data):
        """Edit the last record in the table."""
        try:
            # Hide iframes to avoid click interception
            self.driver.execute_script(
                "document.querySelectorAll('iframe').forEach(iframe => iframe.style.display = 'none');"
            )
            logging.info("Hidden iframes to prevent overlay interference.")
            
            edit_buttons = self.driver.find_elements(*self.locators["edit_buttons"])
            if not edit_buttons:
                raise Exception("No records to edit")

            # Use JavaScript executor to click
            self.driver.execute_script("arguments[0].click();", edit_buttons[-1])
            logging.info("Clicked edit button for the last record")

            # Fill form with updated data
            self.send_keys(self.locators["first_name"], updated_data["first_name"])
            self.send_keys(self.locators["last_name"], updated_data["last_name"])
            self.send_keys(self.locators["email"], updated_data["email"])
            self.send_keys(self.locators["age"], str(updated_data["age"]))
            self.send_keys(self.locators["salary"], str(updated_data["salary"]))
            self.send_keys(self.locators["department"], updated_data["department"])

            # Submit the form
            self.click(self.locators["submit_button"])
            logging.info(f"Edited the last record with data: {updated_data}")
        except Exception as e:
            logging.error(f"Error editing the last record: {e}")
            raise
        
    def delete_last_record(self):
        """Delete the last record in the table."""
        try:
            delete_buttons = self.driver.find_elements(*self.locators["delete_buttons"])
            if not delete_buttons:
                raise Exception("No records to delete")
                
            # Hide iframes to avoid click interception
            self.driver.execute_script(
                "document.querySelectorAll('iframe').forEach(iframe => iframe.style.display = 'none');"
            )
            
            # Use JavaScript executor to click the last delete button
            self.driver.execute_script("arguments[0].click();", delete_buttons[-1])
            logging.info("Deleted the last record successfully")
        except Exception as e:
            logging.error(f"Error during deletion of the last record: {e}")
            raise
            
    def create_dynamic_records(self, records):
        """Create multiple records dynamically."""
        for record in records:
            self.add_new_record(record)
        logging.info(f"Created {len(records)} records dynamically.")

    def delete_all_records(self):
        """Delete all records dynamically from the table."""
        try:
            logging.info("Attempting to delete all records.")
            while True:
                delete_buttons = self.driver.find_elements(*self.locators["delete_buttons"])

                if not delete_buttons:
                    logging.info("No more records to delete.")
                    break

                # Use JavaScript executor to click and add visual delay
                self.driver.execute_script("arguments[0].click();", delete_buttons[0])
                logging.info("Deleted a record using JavaScript executor.")
                time.sleep(1)  # Add delay between deletions
                
        except Exception as e:
            logging.error(f"Error while deleting records: {e}")
            raise