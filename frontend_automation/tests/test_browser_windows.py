import pytest
from pages.browser_windows_page import BrowserWindowsPage
import logging

@pytest.mark.browser_windows
class TestBrowserWindows:
    """Test suite for Browser Windows functionality."""

    @pytest.fixture
    def browser_windows_page(self, driver):
        """Fixture to create and return a BrowserWindowsPage instance."""
        page = BrowserWindowsPage(driver)
        page.open()
        return page

    def test_new_tab(self, browser_windows_page):
        """Test opening a new tab and verifying its content."""
        try:
            browser_windows_page.handle_window_interaction(
                interaction_type="tab",
                expected_text="This is a sample page"
            )
        except Exception as e:
            logging.error(f"Test new tab failed: {e}")
            raise

    def test_new_window(self, browser_windows_page):
        """Test opening a new window and verifying its content."""
        try:
            browser_windows_page.handle_window_interaction(
                interaction_type="window",
                expected_text="This is a sample page"
            )
        except Exception as e:
            logging.error(f"Test new window failed: {e}")
            raise

    def test_new_window_message(self, browser_windows_page):
        """Test opening a new message window and verifying its content."""
        try:
            browser_windows_page.handle_window_interaction(
                interaction_type="message",
                expected_text="Knowledge increases by sharing but not by saving"
            )
        except Exception as e:
            logging.error(f"Test new window message failed: {e}")
            raise