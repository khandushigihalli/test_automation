"""
Facebook Login XPath Finder
This module contains XPath expressions and utility functions to locate Facebook login elements.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class FacebookLoginXPath:
    """
    Class containing XPath expressions for Facebook login elements
    """
    
    # Email/Username input field XPaths (multiple variations)
    EMAIL_XPATHS = [
        "//input[@id='email']",
        "//input[@name='email']",
        "//input[@placeholder='Email or phone number']",
        "//input[@placeholder='Email address or phone number']",
        "//input[@data-testid='royal_email']",
        "//input[contains(@class, 'inputtext') and @type='text']",
        "//input[@aria-label='Email or phone number']",
        "//div[@id='email_container']//input",
        "//form[@id='login_form']//input[@type='text']"
    ]
    
    # Password input field XPaths (multiple variations)
    PASSWORD_XPATHS = [
        "//input[@id='pass']",
        "//input[@name='pass']",
        "//input[@placeholder='Password']",
        "//input[@data-testid='royal_pass']",
        "//input[contains(@class, 'inputtext') and @type='password']",
        "//input[@aria-label='Password']",
        "//div[@id='passContainer']//input",
        "//form[@id='login_form']//input[@type='password']"
    ]
    
    # Login button XPaths (multiple variations)
    LOGIN_BUTTON_XPATHS = [
        "//button[@name='login']",
        "//input[@value='Log In']",
        "//input[@type='submit' and @value='Log In']",
        "//button[@data-testid='royal_login_button']",
        "//button[contains(text(), 'Log In')]",
        "//button[contains(text(), 'Log in')]",
        "//div[@aria-label='Log In']",
        "//input[@id='loginbutton']",
        "//form[@id='login_form']//button[@type='submit']",
        "//a[@role='button' and contains(text(), 'Log In')]"
    ]
    
    # Create account/Sign up button XPaths
    CREATE_ACCOUNT_XPATHS = [
        "//a[contains(text(), 'Create New Account')]",
        "//a[contains(text(), 'Create new account')]",
        "//a[contains(text(), 'Sign Up')]",
        "//button[contains(text(), 'Create New Account')]",
        "//div[@data-testid='open-registration-form-button']",
        "//a[@role='button' and contains(text(), 'Create')]"
    ]
    
    # Forgot password link XPaths
    FORGOT_PASSWORD_XPATHS = [
        "//a[contains(text(), 'Forgot Password')]",
        "//a[contains(text(), 'Forgotten password')]",
        "//a[contains(text(), 'Forgot your password')]",
        "//a[@href and contains(@href, 'recover')]",
        "//div[contains(text(), 'Forgot Password')]//parent::a"
    ]
    
    # Login form container XPaths
    LOGIN_FORM_XPATHS = [
        "//form[@id='login_form']",
        "//div[@id='login_form']",
        "//div[contains(@class, 'login')]",
        "//div[@data-testid='royal_login_form']",
        "//section[contains(@aria-label, 'Log in')]"
    ]
    
    # Error message XPaths
    ERROR_MESSAGE_XPATHS = [
        "//div[@id='error_box']",
        "//div[contains(@class, 'error')]",
        "//div[contains(text(), 'incorrect')]",
        "//div[contains(text(), 'The email address you entered')]",
        "//div[contains(text(), 'The password that you')]",
        "//div[@role='alert']"
    ]

class FacebookLoginFinder:
    """
    Utility class to find Facebook login elements using XPath
    """
    
    def __init__(self, driver=None, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout) if driver else None
    
    def find_element_by_xpath_list(self, xpath_list, wait_for_element=True):
        """
        Try multiple XPath expressions until one is found
        
        Args:
            xpath_list (list): List of XPath expressions to try
            wait_for_element (bool): Whether to wait for element to be present
            
        Returns:
            WebElement or None: Found element or None if not found
        """
        if not self.driver:
            print("Driver not initialized")
            return None
            
        for xpath in xpath_list:
            try:
                if wait_for_element and self.wait:
                    element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                else:
                    element = self.driver.find_element(By.XPATH, xpath)
                print(f"Found element using XPath: {xpath}")
                return element
            except (TimeoutException, NoSuchElementException):
                continue
        
        print("Element not found with any of the provided XPath expressions")
        return None
    
    def find_email_field(self):
        """Find the email/username input field"""
        return self.find_element_by_xpath_list(FacebookLoginXPath.EMAIL_XPATHS)
    
    def find_password_field(self):
        """Find the password input field"""
        return self.find_element_by_xpath_list(FacebookLoginXPath.PASSWORD_XPATHS)
    
    def find_login_button(self):
        """Find the login button"""
        return self.find_element_by_xpath_list(FacebookLoginXPath.LOGIN_BUTTON_XPATHS)
    
    def find_create_account_button(self):
        """Find the create account button"""
        return self.find_element_by_xpath_list(FacebookLoginXPath.CREATE_ACCOUNT_XPATHS)
    
    def find_forgot_password_link(self):
        """Find the forgot password link"""
        return self.find_element_by_xpath_list(FacebookLoginXPath.FORGOT_PASSWORD_XPATHS)
    
    def find_login_form(self):
        """Find the login form container"""
        return self.find_element_by_xpath_list(FacebookLoginXPath.LOGIN_FORM_XPATHS)
    
    def find_error_message(self):
        """Find error message elements"""
        return self.find_element_by_xpath_list(FacebookLoginXPath.ERROR_MESSAGE_XPATHS, wait_for_element=False)
    
    def get_all_login_elements(self):
        """
        Get all login-related elements as a dictionary
        
        Returns:
            dict: Dictionary containing all found elements
        """
        elements = {
            'email_field': self.find_email_field(),
            'password_field': self.find_password_field(),
            'login_button': self.find_login_button(),
            'create_account_button': self.find_create_account_button(),
            'forgot_password_link': self.find_forgot_password_link(),
            'login_form': self.find_login_form(),
            'error_message': self.find_error_message()
        }
        return elements
    
    def print_found_elements(self):
        """Print information about found elements"""
        elements = self.get_all_login_elements()
        
        print("\n=== Facebook Login Elements Found ===")
        for element_name, element in elements.items():
            if element:
                try:
                    tag_name = element.tag_name
                    element_id = element.get_attribute('id') or 'No ID'
                    element_class = element.get_attribute('class') or 'No class'
                    print(f"{element_name}: <{tag_name}> (ID: {element_id}, Class: {element_class})")
                except:
                    print(f"{element_name}: Found but unable to get details")
            else:
                print(f"{element_name}: Not found")

def demo_xpath_usage():
    """
    Demo function showing how to use the XPath finder
    """
    print("=== Facebook Login XPath Demo ===")
    print("\nAvailable XPath expressions:")
    
    print("\n1. Email/Username Field XPaths:")
    for i, xpath in enumerate(FacebookLoginXPath.EMAIL_XPATHS, 1):
        print(f"   {i}. {xpath}")
    
    print("\n2. Password Field XPaths:")
    for i, xpath in enumerate(FacebookLoginXPath.PASSWORD_XPATHS, 1):
        print(f"   {i}. {xpath}")
    
    print("\n3. Login Button XPaths:")
    for i, xpath in enumerate(FacebookLoginXPath.LOGIN_BUTTON_XPATHS, 1):
        print(f"   {i}. {xpath}")
    
    print("\n4. Create Account Button XPaths:")
    for i, xpath in enumerate(FacebookLoginXPath.CREATE_ACCOUNT_XPATHS, 1):
        print(f"   {i}. {xpath}")
    
    print("\n5. Forgot Password Link XPaths:")
    for i, xpath in enumerate(FacebookLoginXPath.FORGOT_PASSWORD_XPATHS, 1):
        print(f"   {i}. {xpath}")

def example_selenium_usage():
    """
    Example of how to use this with Selenium WebDriver
    """
    print("\n=== Example Selenium Usage ===")
    print("""
# Example usage with Selenium WebDriver:

from selenium import webdriver
from facebook_login_xpath import FacebookLoginFinder

# Initialize driver
driver = webdriver.Chrome()  # or Firefox(), Edge(), etc.
driver.get("https://www.facebook.com")

# Initialize the finder
finder = FacebookLoginFinder(driver)

# Find and interact with elements
email_field = finder.find_email_field()
password_field = finder.find_password_field()
login_button = finder.find_login_button()

if email_field and password_field and login_button:
    email_field.send_keys("your_email@example.com")
    password_field.send_keys("your_password")
    login_button.click()

# Print all found elements
finder.print_found_elements()

driver.quit()
    """)

if __name__ == "__main__":
    demo_xpath_usage()
    example_selenium_usage()