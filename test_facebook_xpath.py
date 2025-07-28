"""
Test script for Facebook Login XPath Finder
This script demonstrates how to use the XPath expressions to find Facebook login elements.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sys
from facebook_login_xpath import FacebookLoginFinder, FacebookLoginXPath

def setup_driver(headless=False):
    """
    Setup Chrome WebDriver with options
    
    Args:
        headless (bool): Whether to run in headless mode
        
    Returns:
        webdriver.Chrome: Configured Chrome driver
    """
    chrome_options = Options()
    
    if headless:
        chrome_options.add_argument("--headless")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error setting up Chrome driver: {e}")
        print("Make sure ChromeDriver is installed and in PATH")
        return None

def test_facebook_xpath():
    """
    Test function to find Facebook login elements
    """
    print("=== Testing Facebook Login XPath Finder ===\n")
    
    # Setup driver
    driver = setup_driver(headless=False)
    if not driver:
        return
    
    try:
        # Navigate to Facebook
        print("Navigating to Facebook...")
        driver.get("https://www.facebook.com")
        
        # Wait for page to load
        time.sleep(3)
        
        # Initialize the finder
        finder = FacebookLoginFinder(driver, timeout=10)
        
        # Test individual element finding
        print("Testing individual element finding:")
        print("-" * 40)
        
        # Find email field
        email_field = finder.find_email_field()
        if email_field:
            print("✓ Email field found successfully")
            print(f"  Tag: {email_field.tag_name}")
            print(f"  ID: {email_field.get_attribute('id')}")
            print(f"  Name: {email_field.get_attribute('name')}")
            print(f"  Placeholder: {email_field.get_attribute('placeholder')}")
        else:
            print("✗ Email field not found")
        
        print()
        
        # Find password field
        password_field = finder.find_password_field()
        if password_field:
            print("✓ Password field found successfully")
            print(f"  Tag: {password_field.tag_name}")
            print(f"  ID: {password_field.get_attribute('id')}")
            print(f"  Name: {password_field.get_attribute('name')}")
            print(f"  Type: {password_field.get_attribute('type')}")
        else:
            print("✗ Password field not found")
        
        print()
        
        # Find login button
        login_button = finder.find_login_button()
        if login_button:
            print("✓ Login button found successfully")
            print(f"  Tag: {login_button.tag_name}")
            print(f"  ID: {login_button.get_attribute('id')}")
            print(f"  Name: {login_button.get_attribute('name')}")
            print(f"  Text: {login_button.text}")
            print(f"  Value: {login_button.get_attribute('value')}")
        else:
            print("✗ Login button not found")
        
        print()
        
        # Find create account button
        create_account = finder.find_create_account_button()
        if create_account:
            print("✓ Create account button found successfully")
            print(f"  Tag: {create_account.tag_name}")
            print(f"  Text: {create_account.text}")
        else:
            print("✗ Create account button not found")
        
        print()
        
        # Find forgot password link
        forgot_password = finder.find_forgot_password_link()
        if forgot_password:
            print("✓ Forgot password link found successfully")
            print(f"  Tag: {forgot_password.tag_name}")
            print(f"  Text: {forgot_password.text}")
            print(f"  Href: {forgot_password.get_attribute('href')}")
        else:
            print("✗ Forgot password link not found")
        
        print("\n" + "="*50)
        
        # Print comprehensive summary
        finder.print_found_elements()
        
        print("\n" + "="*50)
        print("Testing all XPath expressions manually:")
        print("-" * 50)
        
        # Test all email XPaths
        print("\nEmail field XPaths:")
        for i, xpath in enumerate(FacebookLoginXPath.EMAIL_XPATHS, 1):
            try:
                element = driver.find_element(By.XPATH, xpath)
                print(f"  ✓ {i:2d}. {xpath}")
            except:
                print(f"  ✗ {i:2d}. {xpath}")
        
        # Test all password XPaths
        print("\nPassword field XPaths:")
        for i, xpath in enumerate(FacebookLoginXPath.PASSWORD_XPATHS, 1):
            try:
                element = driver.find_element(By.XPATH, xpath)
                print(f"  ✓ {i:2d}. {xpath}")
            except:
                print(f"  ✗ {i:2d}. {xpath}")
        
        # Test all login button XPaths
        print("\nLogin button XPaths:")
        for i, xpath in enumerate(FacebookLoginXPath.LOGIN_BUTTON_XPATHS, 1):
            try:
                element = driver.find_element(By.XPATH, xpath)
                print(f"  ✓ {i:2d}. {xpath}")
            except:
                print(f"  ✗ {i:2d}. {xpath}")
        
        print(f"\n{'='*50}")
        print("Test completed successfully!")
        
        # Keep browser open for a few seconds to see results
        print("Keeping browser open for 5 seconds...")
        time.sleep(5)
        
    except Exception as e:
        print(f"Error during testing: {e}")
    
    finally:
        driver.quit()

def test_xpath_without_browser():
    """
    Test function that just prints available XPath expressions
    """
    print("=== Facebook Login XPath Expressions ===\n")
    
    print("EMAIL FIELD XPATHS:")
    for i, xpath in enumerate(FacebookLoginXPath.EMAIL_XPATHS, 1):
        print(f"{i:2d}. {xpath}")
    
    print("\nPASSWORD FIELD XPATHS:")
    for i, xpath in enumerate(FacebookLoginXPath.PASSWORD_XPATHS, 1):
        print(f"{i:2d}. {xpath}")
    
    print("\nLOGIN BUTTON XPATHS:")
    for i, xpath in enumerate(FacebookLoginXPath.LOGIN_BUTTON_XPATHS, 1):
        print(f"{i:2d}. {xpath}")
    
    print("\nCREATE ACCOUNT BUTTON XPATHS:")
    for i, xpath in enumerate(FacebookLoginXPath.CREATE_ACCOUNT_XPATHS, 1):
        print(f"{i:2d}. {xpath}")
    
    print("\nFORGOT PASSWORD LINK XPATHS:")
    for i, xpath in enumerate(FacebookLoginXPath.FORGOT_PASSWORD_XPATHS, 1):
        print(f"{i:2d}. {xpath}")
    
    print("\nERROR MESSAGE XPATHS:")
    for i, xpath in enumerate(FacebookLoginXPath.ERROR_MESSAGE_XPATHS, 1):
        print(f"{i:2d}. {xpath}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--no-browser":
        test_xpath_without_browser()
    else:
        print("Starting Facebook XPath test with browser...")
        print("Use '--no-browser' flag to only see XPath expressions without opening browser\n")
        test_facebook_xpath()