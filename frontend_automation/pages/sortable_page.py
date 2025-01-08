from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
from pages.base_page import BasePage


class SortablePage(BasePage):
    """Page object for the Sortable interaction."""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/sortable"
        self.locators = {
            "sortable_items": (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item"),
            "tab_list": (By.ID, "demo-tab-list"),
        }

    def open(self):
        """Navigate to the Sortable page."""
        self.navigate(self.url)
        logging.info("Opened Sortable page.")

    def switch_to_list_view(self):
        """Ensure the 'List' tab is selected."""
        list_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators["tab_list"])
        )
        list_tab.click()
        logging.info("Switched to List view.")

    def get_sortable_items(self):
        """Retrieve sortable items and their text."""
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.locators["sortable_items"])
        )
        item_texts = [item.text.strip() for item in items if item.text.strip()]
        logging.info(f"Sortable items retrieved: {item_texts}")
        return items, item_texts

    def sort_items(self):
        """Ensure the items are sorted in ascending order using drag-and-drop if needed."""
        action_chains = ActionChains(self.driver)

        # Get initial items and their order
        items, item_texts = self.get_sortable_items()
        sorted_texts = sorted(item_texts)

        if item_texts == sorted_texts:
            logging.info("Items are already sorted in ascending order.")
            return

        logging.info(f"Sorting items to match the expected order: {sorted_texts}")

        # Perform sorting only if necessary
        for target_index, target_text in enumerate(sorted_texts):
            try:
                # Locate the current item and the target position
                current_item = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"//div[@id='demo-tabpane-list']//div[text()='{target_text}']")
                    )
                )
                target_position = items[target_index]

                # Perform drag-and-drop
                action_chains.drag_and_drop(current_item, target_position).perform()
                logging.info(f"Moved item '{target_text}' to position {target_index + 1}.")

                # Wait for DOM to update and re-fetch the list
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located(self.locators["sortable_items"])
                )
                items, item_texts = self.get_sortable_items()

                # Log current state for debugging
                current_order = [item.text for item in items]
                logging.info(f"Current order after move: {current_order}")

            except Exception as e:
                logging.error(f"Error while sorting item '{target_text}': {e}")
                raise

        # Final validation of the sorted order
        final_order = [item.text for item in items]
        assert final_order == sorted_texts, f"Final sorted order is incorrect: {final_order}"
        logging.info("Items sorted in ascending order.")

    def validate_sorting(self):
        """Validate the order of items after sorting."""
        _, item_texts = self.get_sortable_items()
        expected_order = sorted(item_texts)
        assert item_texts == expected_order, f"Items are not sorted correctly: {item_texts}"
        logging.info("Items sorted correctly.")
