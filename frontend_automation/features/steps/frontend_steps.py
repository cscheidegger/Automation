from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.form_page import FormPage
from pages.browser_windows_page import BrowserWindowsPage
from pages.web_tables_page import WebTablesPage
from pages.progress_bar_page import ProgressBarPage
from pages.sortable_page import SortablePage
import logging
import os


# Existing Form Page Steps
@given("I navigate to the Practice Form page")
def step_navigate_to_practice_form_page(context):
    logging.info("Navigating to the Practice Form page.")
    context.form_page = FormPage(context.driver)
    context.form_page.open()


@when("I fill out the form with random data")
def step_fill_out_form(context):
    logging.info("Filling out the Practice Form with random data.")
    try:
        random_data = context.form_page.generate_random_data()
        context.form_page.fill_form(random_data)
        context.random_data = random_data  # Store for later validation
    except Exception as e:
        logging.error(f"Failed to fill out the form: {e}")
        raise


@when("I upload a file")
def step_upload_file(context):
    logging.info("Uploading a file to the Practice Form.")
    try:
        # Use a temporary file
        file_path = "./temp_test_file.txt"
        with open(file_path, "w") as file:
            file.write("Temporary test file content")
        context.form_page.upload_file(file_path)
    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        raise
    finally:
        # Clean up temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
            logging.info("Temporary test file removed.")


@when("I submit the form")
def step_submit_form(context):
    logging.info("Submitting the Practice Form.")
    try:
        context.form_page.submit_form()
    except Exception as e:
        logging.error(f"Error submitting the form: {e}")
        raise


@then("I should see a success popup")
def step_verify_popup(context):
    logging.info("Verifying the success popup on the Practice Form.")
    try:
        assert context.form_page.is_popup_displayed(), "Success popup not displayed."
    except AssertionError as e:
        logging.error(f"Popup verification failed: {e}")
        raise


@then("I close the popup")
def step_close_popup(context):
    logging.info("Closing the success popup.")
    try:
        context.form_page.close_popup()
    except Exception as e:
        logging.error(f"Error closing popup: {e}")
        raise

# New Browser Windows Steps
@given("I navigate to the Browser Windows page")
def step_navigate_browser_windows(context):
    context.browser_windows_page = BrowserWindowsPage(context.driver)
    context.browser_windows_page.open()

@when('I click the "New Window" button')
def step_click_new_window_button(context):
    context.browser_windows_page.click_new_window()

@then('I should see a new window with the message "This is a sample page"')
def step_verify_new_window_message(context):
    new_window_text = context.browser_windows_page.get_new_window_text()
    assert "This is a sample page" in new_window_text, f"Unexpected text: {new_window_text}"

@then("I close the new window")
def step_close_new_window(context):
    context.browser_windows_page.close_new_window_and_switch_back()

# Web Tables
@given("I navigate to the Web Tables page")
def step_navigate_to_web_tables(context):
    context.web_tables_page = WebTablesPage(context.driver)
    context.web_tables_page.navigate_to_web_tables()


@when("I add a new record")
def step_add_new_record(context):
    context.web_tables_page.add_new_record({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "age": 30,
        "salary": 50000,
        "department": "Engineering"
    })


@then("I edit the last record")
def step_edit_last_record(context):
    context.web_tables_page.edit_last_record({
        "first_name": "UpdatedFirst",
        "last_name": "UpdatedLast",
        "email": "updated.email@example.com",
        "age": 35,
        "salary": 60000,
        "department": "UpdatedDepartment"
    })


@then("I delete the last record")
def step_delete_last_record(context):
    try:
        context.web_tables_page.delete_last_record()
        logging.info("Last record deleted successfully")
    except Exception as e:
        logging.error(f"Error during deletion of the last record: {e}")
        raise

@when("I create 12 new records dynamically")
def step_create_dynamic_records(context):
    records = [
        {
            "first_name": f"User{i}",
            "last_name": f"Test{i}",
            "email": f"user{i}@example.com",
            "age": 20 + i,
            "salary": 30000 + (i * 1000),
            "department": f"Department{i}"
        } for i in range(1, 13)
    ]
    context.web_tables_page.create_dynamic_records(records)


@then("I delete all records")
def step_delete_all_records(context):
    try:
        context.web_tables_page.delete_all_records()
        logging.info("All records deleted successfully")
    except Exception as e:
        logging.error(f"Error during deletion of all records: {e}")
        raise

# Progress Bar Page
@given("I navigate to the Progress Bar page")
def step_navigate_to_progress_bar(context):
    context.progress_bar_page = ProgressBarPage(context.driver)
    context.progress_bar_page.navigate_to_progress_bar()

@when("I start the progress bar")
def step_start_progress_bar(context):
    context.progress_bar_page.click_start_button()

@when("I wait for progress to reach {percentage:d} percent")
def step_wait_for_progress(context, percentage):
    context.progress_bar_page.wait_for_progress(percentage)

@then("I verify the progress is not more than {percentage:d} percent")
def step_verify_progress(context, percentage):
    current_progress = context.progress_bar_page.get_progress_value()
    assert current_progress <= percentage, f"Progress {current_progress}% exceeds target {percentage}%"
    logging.info(f"Verified progress {current_progress}% is not more than {percentage}%")

@then("I reset the progress bar")
def step_reset_progress_bar(context):
    context.progress_bar_page.reset_progress_bar()

# Sort Numbers#
@given("I navigate to the Sortable page")
def step_navigate_to_sortable_page(context):
    context.sortable_page = SortablePage(context.driver)
    context.sortable_page.open()

@when("I sort the items in ascending order")
def step_sort_items(context):
    context.sortable_page.switch_to_list_view()
    context.sortable_page.sort_items()

@then("I should see the items sorted correctly")
def step_validate_sorting(context):
    context.sortable_page.validate_sorting()