"""
Comprehensive Selenium WebDriver Examples
This file demonstrates various Selenium automation patterns and best practices.
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest


class SeleniumExamples:
    """Main class containing various Selenium automation examples"""
    
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def setup_driver(self, headless=False, browser="chrome"):
        """
        Setup WebDriver with various options
        
        Args:
            headless (bool): Run browser in headless mode
            browser (str): Browser choice ('chrome', 'firefox', 'edge')
        """
        if browser.lower() == "chrome":
            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            
            self.driver = webdriver.Chrome(options=chrome_options)
        elif browser.lower() == "firefox":
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            firefox_options = FirefoxOptions()
            if headless:
                firefox_options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=firefox_options)
        
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    
    def teardown_driver(self):
        """Close the browser and cleanup"""
        if self.driver:
            self.driver.quit()
    
    def example_google_search(self, search_term):
        """
        Example: Basic Google search automation
        
        Args:
            search_term (str): Term to search for
        """
        try:
            # Navigate to Google
            self.driver.get("https://www.google.com")
            
            # Find search box and enter search term
            search_box = self.wait.until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(search_term)
            search_box.send_keys(Keys.RETURN)
            
            # Wait for results to load
            results = self.wait.until(
                EC.presence_of_element_located((By.ID, "search"))
            )
            
            print(f"Search results found for: {search_term}")
            return True
            
        except TimeoutException:
            print("Timeout waiting for page elements")
            return False
    
    def example_form_automation(self):
        """
        Example: Form filling automation
        """
        try:
            # Navigate to a demo form page
            self.driver.get("https://www.w3schools.com/html/html_forms.asp")
            
            # Example of different input types
            # Text input
            text_input = self.driver.find_element(By.NAME, "firstname")
            text_input.clear()
            text_input.send_keys("John")
            
            # Another text input
            last_name = self.driver.find_element(By.NAME, "lastname")
            last_name.clear()
            last_name.send_keys("Doe")
            
            print("Form filled successfully")
            return True
            
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            return False
    
    def example_dropdown_handling(self):
        """
        Example: Handling dropdown menus
        """
        try:
            # Navigate to a page with dropdowns
            self.driver.get("https://the-internet.herokuapp.com/dropdown")
            
            # Find dropdown element
            dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
            
            # Select by visible text
            dropdown.select_by_visible_text("Option 1")
            time.sleep(1)
            
            # Select by value
            dropdown.select_by_value("2")
            time.sleep(1)
            
            # Select by index
            dropdown.select_by_index(1)
            
            print("Dropdown handling completed")
            return True
            
        except Exception as e:
            print(f"Error handling dropdown: {e}")
            return False
    
    def example_wait_strategies(self):
        """
        Example: Different wait strategies in Selenium
        """
        try:
            self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
            
            # Click start button
            start_button = self.driver.find_element(By.CSS_SELECTOR, "#start button")
            start_button.click()
            
            # Explicit wait - wait for element to be visible
            finish_text = self.wait.until(
                EC.visibility_of_element_located((By.ID, "finish"))
            )
            
            print(f"Text appeared: {finish_text.text}")
            
            # Wait for element to be clickable
            clickable_element = self.wait.until(
                EC.element_to_be_clickable((By.ID, "finish"))
            )
            
            return True
            
        except TimeoutException:
            print("Element did not appear within timeout")
            return False
    
    def example_javascript_execution(self):
        """
        Example: Executing JavaScript in Selenium
        """
        try:
            self.driver.get("https://www.example.com")
            
            # Execute JavaScript to scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Execute JavaScript to get page title
            title = self.driver.execute_script("return document.title;")
            print(f"Page title: {title}")
            
            # Execute JavaScript to click an element
            # self.driver.execute_script("arguments[0].click();", element)
            
            # Execute JavaScript to set value
            # self.driver.execute_script("arguments[0].value = 'test';", input_element)
            
            return True
            
        except Exception as e:
            print(f"JavaScript execution error: {e}")
            return False
    
    def example_mouse_actions(self):
        """
        Example: Mouse actions and interactions
        """
        try:
            self.driver.get("https://the-internet.herokuapp.com/hovers")
            
            # Create ActionChains object
            actions = ActionChains(self.driver)
            
            # Find element to hover over
            hover_element = self.driver.find_element(By.CSS_SELECTOR, ".figure:first-child img")
            
            # Perform hover action
            actions.move_to_element(hover_element).perform()
            
            # Wait for hover effect
            time.sleep(2)
            
            # Double click example
            # actions.double_click(element).perform()
            
            # Right click example
            # actions.context_click(element).perform()
            
            # Drag and drop example
            # source = self.driver.find_element(By.ID, "source")
            # target = self.driver.find_element(By.ID, "target")
            # actions.drag_and_drop(source, target).perform()
            
            print("Mouse actions completed")
            return True
            
        except Exception as e:
            print(f"Mouse actions error: {e}")
            return False
    
    def example_window_handling(self):
        """
        Example: Handling multiple windows/tabs
        """
        try:
            self.driver.get("https://the-internet.herokuapp.com/windows")
            
            # Store current window handle
            main_window = self.driver.current_window_handle
            
            # Click link that opens new window
            new_window_link = self.driver.find_element(By.LINK_TEXT, "Click Here")
            new_window_link.click()
            
            # Wait for new window to open
            self.wait.until(lambda driver: len(driver.window_handles) > 1)
            
            # Switch to new window
            for window_handle in self.driver.window_handles:
                if window_handle != main_window:
                    self.driver.switch_to.window(window_handle)
                    break
            
            # Perform actions in new window
            new_window_text = self.driver.find_element(By.TAG_NAME, "h3").text
            print(f"New window text: {new_window_text}")
            
            # Close new window
            self.driver.close()
            
            # Switch back to main window
            self.driver.switch_to.window(main_window)
            
            return True
            
        except Exception as e:
            print(f"Window handling error: {e}")
            return False
    
    def example_screenshot_capture(self):
        """
        Example: Taking screenshots
        """
        try:
            self.driver.get("https://www.example.com")
            
            # Take full page screenshot
            self.driver.save_screenshot("full_page_screenshot.png")
            
            # Take element screenshot
            element = self.driver.find_element(By.TAG_NAME, "h1")
            element.screenshot("element_screenshot.png")
            
            print("Screenshots captured successfully")
            return True
            
        except Exception as e:
            print(f"Screenshot error: {e}")
            return False
    
    def example_file_upload(self):
        """
        Example: File upload automation
        """
        try:
            self.driver.get("https://the-internet.herokuapp.com/upload")
            
            # Find file input element
            file_input = self.driver.find_element(By.ID, "file-upload")
            
            # Provide path to file (create a dummy file first)
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
                f.write("This is a test file for upload")
                temp_file_path = f.name
            
            # Upload file
            file_input.send_keys(temp_file_path)
            
            # Click upload button
            upload_button = self.driver.find_element(By.ID, "file-submit")
            upload_button.click()
            
            # Verify upload
            success_message = self.wait.until(
                EC.presence_of_element_located((By.ID, "uploaded-files"))
            )
            
            print(f"File uploaded: {success_message.text}")
            
            # Cleanup temp file
            import os
            os.unlink(temp_file_path)
            
            return True
            
        except Exception as e:
            print(f"File upload error: {e}")
            return False


class TestSeleniumExamples(unittest.TestCase):
    """Unit test class for Selenium examples"""
    
    def setUp(self):
        """Setup method called before each test"""
        self.selenium_examples = SeleniumExamples()
        self.selenium_examples.setup_driver(headless=False)
    
    def tearDown(self):
        """Teardown method called after each test"""
        self.selenium_examples.teardown_driver()
    
    def test_google_search(self):
        """Test Google search functionality"""
        result = self.selenium_examples.example_google_search("Selenium WebDriver")
        self.assertTrue(result)
    
    def test_wait_strategies(self):
        """Test wait strategies"""
        result = self.selenium_examples.example_wait_strategies()
        self.assertTrue(result)
    
    def test_dropdown_handling(self):
        """Test dropdown handling"""
        result = self.selenium_examples.example_dropdown_handling()
        self.assertTrue(result)
    
    def test_javascript_execution(self):
        """Test JavaScript execution"""
        result = self.selenium_examples.example_javascript_execution()
        self.assertTrue(result)
    
    def test_mouse_actions(self):
        """Test mouse actions"""
        result = self.selenium_examples.example_mouse_actions()
        self.assertTrue(result)
    
    def test_window_handling(self):
        """Test window handling"""
        result = self.selenium_examples.example_window_handling()
        self.assertTrue(result)
    
    def test_screenshot_capture(self):
        """Test screenshot capture"""
        result = self.selenium_examples.example_screenshot_capture()
        self.assertTrue(result)


# Pytest examples
@pytest.fixture
def selenium_driver():
    """Pytest fixture for Selenium driver"""
    examples = SeleniumExamples()
    examples.setup_driver(headless=True)
    yield examples
    examples.teardown_driver()


def test_google_search_pytest(selenium_driver):
    """Pytest test for Google search"""
    result = selenium_driver.example_google_search("Python Selenium")
    assert result is True


def test_javascript_execution_pytest(selenium_driver):
    """Pytest test for JavaScript execution"""
    result = selenium_driver.example_javascript_execution()
    assert result is True


# Page Object Model Example
class BasePage:
    """Base page class for Page Object Model"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Find element with wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """Click element with wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def enter_text(self, locator, text):
        """Enter text in element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)


class GoogleSearchPage(BasePage):
    """Google search page using Page Object Model"""
    
    # Locators
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    RESULTS = (By.ID, "search")
    
    def search(self, search_term):
        """Perform search"""
        self.enter_text(self.SEARCH_BOX, search_term)
        # Press Enter instead of clicking button (more reliable)
        search_box = self.find_element(self.SEARCH_BOX)
        search_box.send_keys(Keys.RETURN)
    
    def get_results(self):
        """Get search results"""
        return self.find_element(self.RESULTS)


# Data-driven testing example
class DataDrivenTests:
    """Example of data-driven testing with Selenium"""
    
    @staticmethod
    def test_multiple_searches():
        """Test multiple search terms"""
        search_terms = ["Selenium", "Python", "WebDriver", "Automation"]
        
        examples = SeleniumExamples()
        examples.setup_driver(headless=True)
        
        try:
            for term in search_terms:
                print(f"Testing search for: {term}")
                result = examples.example_google_search(term)
                assert result, f"Search failed for term: {term}"
                time.sleep(2)  # Small delay between searches
        finally:
            examples.teardown_driver()


if __name__ == "__main__":
    # Example usage
    print("Starting Selenium Examples...")
    
    # Initialize Selenium examples
    examples = SeleniumExamples()
    examples.setup_driver(headless=False)
    
    try:
        # Run different examples
        print("\n1. Testing Google Search...")
        examples.example_google_search("Selenium WebDriver Python")
        time.sleep(3)
        
        print("\n2. Testing Wait Strategies...")
        examples.example_wait_strategies()
        time.sleep(3)
        
        print("\n3. Testing Dropdown Handling...")
        examples.example_dropdown_handling()
        time.sleep(3)
        
        print("\n4. Testing JavaScript Execution...")
        examples.example_javascript_execution()
        time.sleep(3)
        
        print("\n5. Testing Mouse Actions...")
        examples.example_mouse_actions()
        time.sleep(3)
        
        print("\n6. Testing Window Handling...")
        examples.example_window_handling()
        time.sleep(3)
        
        print("\n7. Testing Screenshot Capture...")
        examples.example_screenshot_capture()
        time.sleep(3)
        
        print("\nAll examples completed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        examples.teardown_driver()
        print("Browser closed.")