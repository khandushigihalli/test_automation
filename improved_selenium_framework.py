"""
Improved Selenium Framework
This builds upon your existing framework with modern Selenium practices
"""

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    TimeoutException, 
    NoSuchElementException, 
    ElementNotInteractableException,
    WebDriverException
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ImprovedDriverManager:
    """Enhanced driver management with better configuration"""
    
    @staticmethod
    def get_chrome_driver(headless=False, download_path=None):
        """Get Chrome driver with optimized options"""
        chrome_options = Options()
        
        if headless:
            chrome_options.add_argument("--headless")
        
        # Performance optimizations
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-images")  # Faster loading
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Download preferences
        if download_path:
            prefs = {
                "download.default_directory": download_path,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }
            chrome_options.add_experimental_option("prefs", prefs)
        
        # Suppress logging
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return driver


class EnhancedBasePage:
    """Enhanced base page with better error handling and utilities"""
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
        
    def find_element(self, locator, timeout=None):
        """Find element with custom timeout"""
        wait_time = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator, timeout=None):
        """Find multiple elements"""
        wait_time = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator, timeout=None):
        """Click element with wait and error handling"""
        try:
            wait_time = timeout or self.timeout
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"Successfully clicked element: {locator}")
            return True
        except TimeoutException:
            logger.error(f"Element not clickable within {wait_time} seconds: {locator}")
            return False
        except ElementNotInteractableException:
            logger.error(f"Element not interactable: {locator}")
            # Try JavaScript click as fallback
            return self.js_click(locator)
    
    def js_click(self, locator):
        """Click element using JavaScript"""
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
            logger.info(f"JavaScript click successful: {locator}")
            return True
        except Exception as e:
            logger.error(f"JavaScript click failed: {e}")
            return False
    
    def enter_text(self, locator, text, clear_first=True, timeout=None):
        """Enter text with better error handling"""
        try:
            wait_time = timeout or self.timeout
            wait = WebDriverWait(self.driver, wait_time)
            element = wait.until(EC.element_to_be_clickable(locator))
            
            if clear_first:
                element.clear()
            
            element.send_keys(text)
            logger.info(f"Successfully entered text in element: {locator}")
            return True
        except Exception as e:
            logger.error(f"Failed to enter text: {e}")
            return False
    
    def get_text(self, locator, timeout=None):
        """Get element text with error handling"""
        try:
            element = self.find_element(locator, timeout)
            return element.text
        except Exception as e:
            logger.error(f"Failed to get text: {e}")
            return None
    
    def get_attribute(self, locator, attribute, timeout=None):
        """Get element attribute"""
        try:
            element = self.find_element(locator, timeout)
            return element.get_attribute(attribute)
        except Exception as e:
            logger.error(f"Failed to get attribute: {e}")
            return None
    
    def is_element_present(self, locator, timeout=2):
        """Check if element is present"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_visible(self, locator, timeout=2):
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=None):
        """Wait for element to disappear"""
        wait_time = timeout or self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            logger.warning(f"Element did not disappear: {locator}")
            return False
    
    def select_dropdown_by_text(self, locator, text, timeout=None):
        """Select dropdown option by visible text"""
        try:
            element = self.find_element(locator, timeout)
            select = Select(element)
            select.select_by_visible_text(text)
            logger.info(f"Selected dropdown option: {text}")
            return True
        except Exception as e:
            logger.error(f"Failed to select dropdown: {e}")
            return False
    
    def select_dropdown_by_value(self, locator, value, timeout=None):
        """Select dropdown option by value"""
        try:
            element = self.find_element(locator, timeout)
            select = Select(element)
            select.select_by_value(value)
            logger.info(f"Selected dropdown value: {value}")
            return True
        except Exception as e:
            logger.error(f"Failed to select dropdown: {e}")
            return False
    
    def scroll_to_element(self, locator):
        """Scroll to element"""
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return True
        except Exception as e:
            logger.error(f"Failed to scroll to element: {e}")
            return False
    
    def hover_over_element(self, locator, timeout=None):
        """Hover over element"""
        try:
            element = self.find_element(locator, timeout)
            ActionChains(self.driver).move_to_element(element).perform()
            logger.info(f"Hovered over element: {locator}")
            return True
        except Exception as e:
            logger.error(f"Failed to hover: {e}")
            return False
    
    def double_click(self, locator, timeout=None):
        """Double click element"""
        try:
            element = self.find_element(locator, timeout)
            ActionChains(self.driver).double_click(element).perform()
            logger.info(f"Double clicked element: {locator}")
            return True
        except Exception as e:
            logger.error(f"Failed to double click: {e}")
            return False
    
    def right_click(self, locator, timeout=None):
        """Right click element"""
        try:
            element = self.find_element(locator, timeout)
            ActionChains(self.driver).context_click(element).perform()
            logger.info(f"Right clicked element: {locator}")
            return True
        except Exception as e:
            logger.error(f"Failed to right click: {e}")
            return False
    
    def switch_to_frame(self, frame_locator):
        """Switch to iframe"""
        try:
            frame = self.find_element(frame_locator)
            self.driver.switch_to.frame(frame)
            logger.info("Switched to frame")
            return True
        except Exception as e:
            logger.error(f"Failed to switch to frame: {e}")
            return False
    
    def switch_to_default_content(self):
        """Switch back to default content"""
        try:
            self.driver.switch_to.default_content()
            logger.info("Switched to default content")
            return True
        except Exception as e:
            logger.error(f"Failed to switch to default content: {e}")
            return False
    
    def take_screenshot(self, filename):
        """Take screenshot"""
        try:
            self.driver.save_screenshot(filename)
            logger.info(f"Screenshot saved: {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return False
    
    def execute_javascript(self, script, *args):
        """Execute JavaScript"""
        try:
            return self.driver.execute_script(script, *args)
        except Exception as e:
            logger.error(f"JavaScript execution failed: {e}")
            return None


class ImprovedLoginPage(EnhancedBasePage):
    """Improved login page with modern locators and methods"""
    
    # Modern locators using different strategies
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://35.154.213.24"  # Your existing URL
    
    def navigate_to_login(self):
        """Navigate to login page"""
        try:
            self.driver.get(self.url)
            logger.info(f"Navigated to: {self.url}")
            return True
        except Exception as e:
            logger.error(f"Failed to navigate: {e}")
            return False
    
    def login(self, username, password):
        """Perform login with error handling"""
        try:
            # Enter username
            if not self.enter_text(self.USERNAME_INPUT, username):
                return False
            
            # Enter password
            if not self.enter_text(self.PASSWORD_INPUT, password):
                return False
            
            # Click login button
            if not self.click_element(self.LOGIN_BUTTON):
                return False
            
            # Wait for either success or error
            time.sleep(2)  # Small wait for response
            
            if self.is_element_present(self.ERROR_MESSAGE):
                error_text = self.get_text(self.ERROR_MESSAGE)
                logger.error(f"Login failed: {error_text}")
                return False
            
            logger.info("Login successful")
            return True
            
        except Exception as e:
            logger.error(f"Login process failed: {e}")
            return False
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
    
    def is_login_page_loaded(self):
        """Check if login page is loaded"""
        return self.is_element_present(self.LOGIN_BUTTON, timeout=5)


class TestDataManager:
    """Manage test data"""
    
    @staticmethod
    def get_valid_credentials():
        """Get valid test credentials"""
        return {
            "username": "9108668521",
            "password": "khan8521"
        }
    
    @staticmethod
    def get_invalid_credentials():
        """Get invalid test credentials"""
        return [
            {"username": "invalid", "password": "invalid"},
            {"username": "", "password": ""},
            {"username": "1234567890", "password": "wrongpass"}
        ]


class SeleniumTestRunner:
    """Test runner with better reporting"""
    
    def __init__(self, headless=False):
        self.driver = None
        self.headless = headless
        self.test_results = []
    
    def setup(self):
        """Setup test environment"""
        try:
            self.driver = ImprovedDriverManager.get_chrome_driver(headless=self.headless)
            logger.info("Driver setup successful")
            return True
        except Exception as e:
            logger.error(f"Driver setup failed: {e}")
            return False
    
    def teardown(self):
        """Cleanup test environment"""
        if self.driver:
            self.driver.quit()
            logger.info("Driver closed")
    
    def run_login_tests(self):
        """Run comprehensive login tests"""
        login_page = ImprovedLoginPage(self.driver)
        
        # Test 1: Valid login
        test_name = "Valid Login Test"
        logger.info(f"Running: {test_name}")
        
        if login_page.navigate_to_login():
            if login_page.is_login_page_loaded():
                credentials = TestDataManager.get_valid_credentials()
                result = login_page.login(credentials["username"], credentials["password"])
                self.test_results.append({"test": test_name, "result": result})
            else:
                self.test_results.append({"test": test_name, "result": False})
        else:
            self.test_results.append({"test": test_name, "result": False})
        
        # Test 2: Invalid login tests
        invalid_credentials = TestDataManager.get_invalid_credentials()
        
        for i, creds in enumerate(invalid_credentials):
            test_name = f"Invalid Login Test {i+1}"
            logger.info(f"Running: {test_name}")
            
            login_page.navigate_to_login()
            if login_page.is_login_page_loaded():
                # For invalid credentials, we expect login to fail (return False)
                result = not login_page.login(creds["username"], creds["password"])
                self.test_results.append({"test": test_name, "result": result})
            else:
                self.test_results.append({"test": test_name, "result": False})
    
    def generate_report(self):
        """Generate test report"""
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result["result"])
        failed_tests = total_tests - passed_tests
        
        print("\n" + "="*50)
        print("TEST EXECUTION REPORT")
        print("="*50)
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        print("\nDetailed Results:")
        print("-"*50)
        
        for result in self.test_results:
            status = "PASS" if result["result"] else "FAIL"
            print(f"{result['test']}: {status}")
        
        print("="*50)


# Example usage and main execution
if __name__ == "__main__":
    print("Starting Improved Selenium Framework Demo...")
    
    # Create test runner
    runner = SeleniumTestRunner(headless=False)
    
    try:
        # Setup
        if runner.setup():
            # Run tests
            runner.run_login_tests()
            
            # Generate report
            runner.generate_report()
        else:
            print("Failed to setup test environment")
    
    except Exception as e:
        logger.error(f"Test execution failed: {e}")
    
    finally:
        # Cleanup
        runner.teardown()
        print("Test execution completed.")