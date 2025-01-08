from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import string
import os
import logging


class FormPage:
    """Page Object for the Practice Form page."""

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

        # Locators for form fields
        self.locators = {
            "first_name": (By.ID, "firstName"),
            "last_name": (By.ID, "lastName"),
            "email": (By.ID, "userEmail"),
            "gender_male": (By.XPATH, "//label[contains(text(),'Male')]"),
            "mobile": (By.ID, "userNumber"),
            "date_of_birth": (By.ID, "dateOfBirthInput"),
            "subjects": (By.ID, "subjectsInput"),
            "hobbies_sports": (By.XPATH, "//label[contains(text(),'Sports')]"),
            "upload_picture": (By.ID, "uploadPicture"),
            "address": (By.ID, "currentAddress"),
            "state": (By.ID, "state"),
            "city": (By.ID, "city"),
            "submit": (By.ID, "submit"),
            "popup_modal": (By.CSS_SELECTOR, ".modal-content"),
            "close_button": (By.ID, "closeLargeModal"),
        }

    def open(self):
        """Open the Practice Form page."""
        logging.info(f"Navigating to URL: {self.url}")
        self.driver.get(self.url)

    def generate_random_data(self):
        """Generate random data for the form."""
        return {
            "first_name": ''.join(random.choices(string.ascii_letters, k=8)),
            "last_name": ''.join(random.choices(string.ascii_letters, k=10)),
            "email": ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com",
            "mobile": ''.join(random.choices(string.digits, k=10)),
            "address": ''.join(random.choices(string.ascii_letters + string.digits + " ", k=20)),
            "date_of_birth": "06 Jan 1990",  # Example static date
        }

    def fill_form(self, data):
        """Fill the form with provided data."""
        try:
            self.driver.find_element(*self.locators["first_name"]).send_keys(data["first_name"])
            self.driver.find_element(*self.locators["last_name"]).send_keys(data["last_name"])
            self.driver.find_element(*self.locators["email"]).send_keys(data["email"])
            self.driver.find_element(*self.locators["mobile"]).send_keys(data["mobile"])

            # Set Date of Birth
            date_of_birth_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators["date_of_birth"])
            )
            date_of_birth_input.clear()
            date_of_birth_input.send_keys(data["date_of_birth"])
            date_of_birth_input.send_keys(Keys.ESCAPE)  # Close the date picker

            # Gender
            self.driver.find_element(*self.locators["gender_male"]).click()

            # Subjects
            subjects_input = self.driver.find_element(*self.locators["subjects"])
            subjects_input.send_keys("Maths")
            subjects_input.send_keys(Keys.ENTER)

            # Hobbies
            hobbies_checkbox = self.driver.find_element(*self.locators["hobbies_sports"])
            self.driver.execute_script("arguments[0].checked = true;", hobbies_checkbox)

            # Address
            self.driver.find_element(*self.locators["address"]).send_keys(data["address"])

            logging.info("Form filled successfully.")
        except Exception as e:
            logging.error(f"Error filling the form: {e}")
            raise

    def upload_file(self, file_path):
        """Uploads a file."""
        try:
            absolute_path = os.path.abspath(file_path)
            logging.info(f"Uploading file from path: {absolute_path}")
            self.driver.find_element(*self.locators["upload_picture"]).send_keys(absolute_path)
            logging.info("File uploaded successfully.")
        except Exception as e:
            logging.error(f"Error uploading file: {e}")
            raise

    def submit_form(self):
        """Submit the form."""
        try:
            # Remove obstructing iframes
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            for iframe in iframes:
                self.driver.execute_script("arguments[0].remove();", iframe)

            # Scroll to the submit button
            submit_button = self.driver.find_element(*self.locators["submit"])
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

            # Attempt to click
            submit_button.click()
            logging.info("Form submitted successfully.")
        except Exception as e:
            logging.error(f"Error submitting the form: {e}")
            raise

    def is_popup_displayed(self):
        """Check if the success popup is displayed."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locators["popup_modal"]))
            logging.info("Success popup is displayed.")
            return True
        except Exception as e:
            logging.error(f"Error verifying success popup: {e}")
            return False

    def close_popup(self):
        """Close the success popup."""
        try:
            # Remove obstructing iframes or overlapping elements
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            for iframe in iframes:
                self.driver.execute_script("arguments[0].remove();", iframe)
                logging.info("Removed an obstructing iframe.")

            # Remove specific ad elements if present
            ad_elements = self.driver.find_elements(By.CSS_SELECTOR, "[id^='google_ads_iframe']")
            for ad in ad_elements:
                self.driver.execute_script("arguments[0].remove();", ad)
                logging.info("Removed an obstructing ad element.")

            # Scroll to the close button to ensure visibility
            close_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators["close_button"])
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", close_button)

            # Retry clicking using JavaScript to bypass potential interception
            self.driver.execute_script("arguments[0].click();", close_button)
            logging.info("Popup closed successfully.")
        except Exception as e:
            logging.error(f"Error closing popup: {e}")
            raise