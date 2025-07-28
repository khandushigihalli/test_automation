"""
Simple Facebook Login XPath Demo
This script shows XPath expressions for Facebook login elements without requiring Selenium.
"""

class FacebookLoginXPaths:
    """
    Collection of XPath expressions for Facebook login elements
    """
    
    # Most commonly used and reliable XPath expressions
    EMAIL_XPATH_PRIMARY = "//input[@id='email']"
    PASSWORD_XPATH_PRIMARY = "//input[@id='pass']"
    LOGIN_BUTTON_XPATH_PRIMARY = "//button[@name='login']"
    
    # Alternative XPath expressions for email field
    EMAIL_XPATHS = [
        "//input[@id='email']",                                    # Standard ID
        "//input[@name='email']",                                  # Standard name
        "//input[@placeholder='Email or phone number']",          # Placeholder text
        "//input[@placeholder='Email address or phone number']",  # Alternative placeholder
        "//input[@data-testid='royal_email']",                    # Test ID
        "//input[contains(@class, 'inputtext') and @type='text']", # Class + type
        "//input[@aria-label='Email or phone number']",           # Accessibility label
        "//div[@id='email_container']//input",                    # Container based
        "//form[@id='login_form']//input[@type='text']"           # Form based
    ]
    
    # Alternative XPath expressions for password field
    PASSWORD_XPATHS = [
        "//input[@id='pass']",                                     # Standard ID
        "//input[@name='pass']",                                   # Standard name
        "//input[@placeholder='Password']",                        # Placeholder text
        "//input[@data-testid='royal_pass']",                     # Test ID
        "//input[contains(@class, 'inputtext') and @type='password']", # Class + type
        "//input[@aria-label='Password']",                         # Accessibility label
        "//div[@id='passContainer']//input",                       # Container based
        "//form[@id='login_form']//input[@type='password']"        # Form based
    ]
    
    # Alternative XPath expressions for login button
    LOGIN_BUTTON_XPATHS = [
        "//button[@name='login']",                                 # Standard name
        "//input[@value='Log In']",                                # Input button with value
        "//input[@type='submit' and @value='Log In']",            # Submit input
        "//button[@data-testid='royal_login_button']",            # Test ID
        "//button[contains(text(), 'Log In')]",                   # Text content
        "//button[contains(text(), 'Log in')]",                   # Alternative text
        "//div[@aria-label='Log In']",                             # Accessibility label
        "//input[@id='loginbutton']",                              # ID based
        "//form[@id='login_form']//button[@type='submit']",       # Form based
        "//a[@role='button' and contains(text(), 'Log In')]"      # Link as button
    ]
    
    # XPath expressions for other elements
    CREATE_ACCOUNT_XPATHS = [
        "//a[contains(text(), 'Create New Account')]",
        "//a[contains(text(), 'Create new account')]",
        "//a[contains(text(), 'Sign Up')]",
        "//button[contains(text(), 'Create New Account')]",
        "//div[@data-testid='open-registration-form-button']"
    ]
    
    FORGOT_PASSWORD_XPATHS = [
        "//a[contains(text(), 'Forgot Password')]",
        "//a[contains(text(), 'Forgotten password')]",
        "//a[contains(text(), 'Forgot your password')]",
        "//a[@href and contains(@href, 'recover')]"
    ]

def print_xpath_categories():
    """Print all XPath expressions organized by categories"""
    
    print("=" * 60)
    print("FACEBOOK LOGIN XPATH EXPRESSIONS")
    print("=" * 60)
    
    print("\n🔹 PRIMARY/MOST RELIABLE XPATHS:")
    print(f"   Email Field:    {FacebookLoginXPaths.EMAIL_XPATH_PRIMARY}")
    print(f"   Password Field: {FacebookLoginXPaths.PASSWORD_XPATH_PRIMARY}")
    print(f"   Login Button:   {FacebookLoginXPaths.LOGIN_BUTTON_XPATH_PRIMARY}")
    
    print(f"\n📧 EMAIL FIELD XPATHS ({len(FacebookLoginXPaths.EMAIL_XPATHS)} variations):")
    for i, xpath in enumerate(FacebookLoginXPaths.EMAIL_XPATHS, 1):
        print(f"   {i:2d}. {xpath}")
    
    print(f"\n🔒 PASSWORD FIELD XPATHS ({len(FacebookLoginXPaths.PASSWORD_XPATHS)} variations):")
    for i, xpath in enumerate(FacebookLoginXPaths.PASSWORD_XPATHS, 1):
        print(f"   {i:2d}. {xpath}")
    
    print(f"\n🔘 LOGIN BUTTON XPATHS ({len(FacebookLoginXPaths.LOGIN_BUTTON_XPATHS)} variations):")
    for i, xpath in enumerate(FacebookLoginXPaths.LOGIN_BUTTON_XPATHS, 1):
        print(f"   {i:2d}. {xpath}")
    
    print(f"\n➕ CREATE ACCOUNT BUTTON XPATHS ({len(FacebookLoginXPaths.CREATE_ACCOUNT_XPATHS)} variations):")
    for i, xpath in enumerate(FacebookLoginXPaths.CREATE_ACCOUNT_XPATHS, 1):
        print(f"   {i:2d}. {xpath}")
    
    print(f"\n❓ FORGOT PASSWORD LINK XPATHS ({len(FacebookLoginXPaths.FORGOT_PASSWORD_XPATHS)} variations):")
    for i, xpath in enumerate(FacebookLoginXPaths.FORGOT_PASSWORD_XPATHS, 1):
        print(f"   {i:2d}. {xpath}")

def print_usage_examples():
    """Print usage examples for different automation tools"""
    
    print("\n" + "=" * 60)
    print("USAGE EXAMPLES")
    print("=" * 60)
    
    print("\n🔧 SELENIUM WEBDRIVER EXAMPLE:")
    print("""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

# Find elements using XPath
email_field = driver.find_element(By.XPATH, "//input[@id='email']")
password_field = driver.find_element(By.XPATH, "//input[@id='pass']")
login_button = driver.find_element(By.XPATH, "//button[@name='login']")

# Interact with elements
email_field.send_keys("your_email@example.com")
password_field.send_keys("your_password")
login_button.click()
""")
    
    print("\n🔧 PLAYWRIGHT EXAMPLE:")
    print("""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.facebook.com")
    
    # Find elements using XPath
    page.fill("xpath=//input[@id='email']", "your_email@example.com")
    page.fill("xpath=//input[@id='pass']", "your_password")
    page.click("xpath=//button[@name='login']")
""")
    
    print("\n🔧 REQUESTS + BEAUTIFULSOUP EXAMPLE:")
    print("""
import requests
from bs4 import BeautifulSoup

# Get the page
response = requests.get("https://www.facebook.com")
soup = BeautifulSoup(response.content, 'html.parser')

# Find elements (convert XPath to CSS selector or use find methods)
email_field = soup.find('input', {'id': 'email'})
password_field = soup.find('input', {'id': 'pass'})
login_button = soup.find('button', {'name': 'login'})
""")

def print_xpath_tips():
    """Print tips for using XPath effectively"""
    
    print("\n" + "=" * 60)
    print("XPATH TIPS & BEST PRACTICES")
    print("=" * 60)
    
    tips = [
        "🎯 Start with the most specific and reliable selectors (ID, name attributes)",
        "🔄 Have multiple backup XPath expressions in case Facebook changes their HTML",
        "⚡ Use contains() function for partial text matching: contains(text(), 'Log')",
        "🏷️  Prefer data-testid attributes as they're more stable than classes",
        "🎨 Avoid using CSS classes as primary selectors (they change frequently)",
        "🔍 Use browser developer tools to test XPath expressions",
        "⏱️  Add explicit waits when automating to handle dynamic loading",
        "🛡️  Always handle exceptions when elements are not found",
        "📱 Remember that mobile Facebook may have different XPaths",
        "🌐 Facebook's interface varies by region and A/B testing"
    ]
    
    for tip in tips:
        print(f"   {tip}")

def print_xpath_testing_commands():
    """Print commands to test XPath expressions in browser console"""
    
    print("\n" + "=" * 60)
    print("TESTING XPATH IN BROWSER CONSOLE")
    print("=" * 60)
    
    print("\n💻 Open Facebook in browser, press F12, go to Console tab, and try:")
    print("""
// Test if email field exists
$x("//input[@id='email']")

// Test if password field exists  
$x("//input[@id='pass']")

// Test if login button exists
$x("//button[@name='login']")

// Count how many elements match
$x("//input[@id='email']").length

// Get element attributes
$x("//input[@id='email']")[0].getAttribute('placeholder')
""")

if __name__ == "__main__":
    print_xpath_categories()
    print_usage_examples()
    print_xpath_tips()
    print_xpath_testing_commands()
    
    print(f"\n{'=' * 60}")
    print("✅ Facebook Login XPath Reference Complete!")
    print("💡 Save this reference for your web automation projects.")
    print(f"{'=' * 60}")