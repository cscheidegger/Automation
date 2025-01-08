import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.web_tables_page import WebTablesPage  # Ensure the path is correct

# Configure logging
logging.basicConfig(level=logging.INFO)

def before_scenario(context, scenario):
    """Setup WebDriver before each scenario."""
    logging.info(f"Setting up WebDriver for scenario: {scenario.name}")
    
    try:
        # Path to the ChromeDriver
        chromedriver_path = r"C:\Users\csche\Downloads\qa_automation\frontend_automation\drivers\chromedriver.exe"
        if not os.path.exists(chromedriver_path):
            raise FileNotFoundError(f"Chromedriver not found at {chromedriver_path}. Please update the path.")
        
        # Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        
        # Initialize WebDriver with options
        service = Service(chromedriver_path)
        context.driver = webdriver.Chrome(service=service, options=chrome_options)
        context.driver.implicitly_wait(10)  # Adding implicit wait for stability
        logging.info("WebDriver initialized successfully.")
        
        # Attach the WebTablesPage to the context for step definitions
        context.web_tables_page = WebTablesPage(context.driver)
    except Exception as e:
        logging.error(f"Error initializing WebDriver: {e}")
        raise

def after_scenario(context, scenario):
    """Quit WebDriver after each scenario."""
    if hasattr(context, "driver"):
        try:
            context.driver.quit()
            logging.info("WebDriver session ended.")
        except Exception as e:
            logging.warning(f"Error during WebDriver teardown: {e}")
