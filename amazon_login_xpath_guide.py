#!/usr/bin/env python3
"""
Amazon Login XPath Elements Guide
=================================

This guide provides XPath selectors for Amazon login automation.
Note: Amazon has implemented strict anti-bot measures as of late 2024.

WARNING: Always respect Amazon's Terms of Service and robots.txt.
Use these selectors responsibly and consider legal implications.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class AmazonLoginXPaths:
    """
    XPath selectors for Amazon login elements.
    These may change frequently as Amazon updates their UI.
    """
    
    # Main login page elements
    EMAIL_INPUT = "//input[@id='ap_email']"
    EMAIL_INPUT_ALT = "//input[@name='email']"
    EMAIL_INPUT_XPATH = "//input[@type='email']"
    
    CONTINUE_BUTTON = "//input[@id='continue']"
    CONTINUE_BUTTON_ALT = "//span[@id='continue']"
    
    # Password page elements
    PASSWORD_INPUT = "//input[@id='ap_password']"
    PASSWORD_INPUT_ALT = "//input[@name='password']"
    PASSWORD_INPUT_TYPE = "//input[@type='password']"
    
    SIGNIN_BUTTON = "//input[@id='signInSubmit']"
    SIGNIN_BUTTON_ALT = "//span[@id='auth-signin-button']"
    SIGNIN_BUTTON_SPAN = "//span[contains(text(), 'Sign in')]"
    
    # Two-factor authentication elements
    OTP_INPUT = "//input[@id='auth-mfa-otpcode']"
    OTP_INPUT_ALT = "//input[@name='otpCode']"
    
    OTP_SUBMIT = "//input[@id='auth-signin-button']"
    OTP_SUBMIT_ALT = "//span[@id='auth-signin-button']"
    
    # CAPTCHA elements
    CAPTCHA_IMAGE = "//img[contains(@src, 'captcha')]"
    CAPTCHA_INPUT = "//input[@id='captchacharacters']"
    CAPTCHA_INPUT_ALT = "//input[@name='field-keywords']"
    
    # Error messages
    ERROR_MESSAGE = "//div[@id='auth-error-message-box']"
    ERROR_MESSAGE_ALT = "//span[@class='a-list-item']"
    EMAIL_ERROR = "//div[contains(@class, 'auth-inlined-error-message')]"
    
    # Account selection (multiple accounts)
    ACCOUNT_PICKER = "//div[@data-testid='account-picker']"
    ACCOUNT_OPTION = "//div[@data-testid='account-picker-account']"
    
    # Remember me checkbox
    REMEMBER_ME = "//input[@name='rememberMe']"
    REMEMBER_ME_LABEL = "//label[@for='ap_signin_existing_radio']"
    
    # Create account link
    CREATE_ACCOUNT = "//a[@id='createAccountSubmit']"
    CREATE_ACCOUNT_ALT = "//a[contains(text(), 'Create your Amazon account')]"
    
    # Forgot password
    FORGOT_PASSWORD = "//a[@id='auth-fpp-link-bottom']"
    FORGOT_PASSWORD_ALT = "//a[contains(text(), 'Forgot your password')]"
    
    # Business account
    BUSINESS_SIGNIN = "//a[contains(@href, 'business')]"
    
    # Mobile-specific elements
    MOBILE_EMAIL = "//input[@data-testid='email']"
    MOBILE_PASSWORD = "//input[@data-testid='password']"
    MOBILE_SIGNIN = "//button[@data-testid='signin-button']"

class AmazonLoginAutomation:
    """
    Example implementation of Amazon login automation.
    Use responsibly and in accordance with Amazon's Terms of Service.
    """
    
    def __init__(self, headless=False):
        self.setup_driver(headless)
        self.wait = WebDriverWait(self.driver, 10)
    
    def setup_driver(self, headless=False):
        """Setup Chrome driver with appropriate options"""
        options = webdriver.ChromeOptions()
        
        if headless:
            options.add_argument('--headless')
        
        # Anti-detection measures
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # User agent to avoid detection
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    def navigate_to_login(self, region='com'):
        """Navigate to Amazon login page"""
        login_url = f"https://www.amazon.{region}/ap/signin"
        self.driver.get(login_url)
        time.sleep(2)  # Allow page to load
    
    def enter_email(self, email):
        """Enter email address"""
        try:
            # Try primary email input
            email_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, AmazonLoginXPaths.EMAIL_INPUT))
            )
        except:
            # Try alternative email input
            email_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, AmazonLoginXPaths.EMAIL_INPUT_ALT))
            )
        
        email_input.clear()
        email_input.send_keys(email)
        
        # Click continue button
        try:
            continue_btn = self.driver.find_element(By.XPATH, AmazonLoginXPaths.CONTINUE_BUTTON)
            continue_btn.click()
        except:
            continue_btn = self.driver.find_element(By.XPATH, AmazonLoginXPaths.CONTINUE_BUTTON_ALT)
            continue_btn.click()
        
        time.sleep(2)
    
    def enter_password(self, password):
        """Enter password"""
        try:
            password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, AmazonLoginXPaths.PASSWORD_INPUT))
            )
        except:
            password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, AmazonLoginXPaths.PASSWORD_INPUT_ALT))
            )
        
        password_input.clear()
        password_input.send_keys(password)
        
        # Click sign in button
        try:
            signin_btn = self.driver.find_element(By.XPATH, AmazonLoginXPaths.SIGNIN_BUTTON)
            signin_btn.click()
        except:
            signin_btn = self.driver.find_element(By.XPATH, AmazonLoginXPaths.SIGNIN_BUTTON_ALT)
            signin_btn.click()
        
        time.sleep(2)
    
    def handle_2fa(self, otp_code):
        """Handle two-factor authentication"""
        try:
            otp_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, AmazonLoginXPaths.OTP_INPUT))
            )
            otp_input.clear()
            otp_input.send_keys(otp_code)
            
            otp_submit = self.driver.find_element(By.XPATH, AmazonLoginXPaths.OTP_SUBMIT)
            otp_submit.click()
            
            time.sleep(2)
            return True
        except:
            return False
    
    def check_for_captcha(self):
        """Check if CAPTCHA is present"""
        try:
            captcha = self.driver.find_element(By.XPATH, AmazonLoginXPaths.CAPTCHA_IMAGE)
            return True
        except:
            return False
    
    def get_error_message(self):
        """Get any error messages"""
        try:
            error = self.driver.find_element(By.XPATH, AmazonLoginXPaths.ERROR_MESSAGE)
            return error.text
        except:
            try:
                error = self.driver.find_element(By.XPATH, AmazonLoginXPaths.ERROR_MESSAGE_ALT)
                return error.text
            except:
                return None
    
    def is_logged_in(self):
        """Check if successfully logged in"""
        try:
            # Look for account menu or user name
            self.driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
            return True
        except:
            return False
    
    def close(self):
        """Close the browser"""
        self.driver.quit()

# Alternative XPath strategies for different Amazon pages
AMAZON_LOGIN_XPATHS_COMPREHENSIVE = {
    # Standard login page
    'standard': {
        'email': [
            "//input[@id='ap_email']",
            "//input[@name='email']",
            "//input[@type='email']",
            "//input[@placeholder='Email or mobile phone number']"
        ],
        'continue': [
            "//input[@id='continue']",
            "//span[@id='continue']",
            "//button[contains(text(), 'Continue')]"
        ],
        'password': [
            "//input[@id='ap_password']",
            "//input[@name='password']",
            "//input[@type='password']"
        ],
        'signin': [
            "//input[@id='signInSubmit']",
            "//span[@id='auth-signin-button']",
            "//button[contains(text(), 'Sign in')]"
        ]
    },
    
    # Mobile login page
    'mobile': {
        'email': [
            "//input[@data-testid='email']",
            "//input[@id='ap_email_login']",
            "//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']"
        ],
        'password': [
            "//input[@data-testid='password']",
            "//input[@id='ap_password']"
        ],
        'signin': [
            "//button[@data-testid='signin-button']",
            "//input[@id='signInSubmit']"
        ]
    },
    
    # Business login
    'business': {
        'email': [
            "//input[@id='ap_email']",
            "//input[@name='email']"
        ],
        'signin': [
            "//input[@id='signInSubmit']",
            "//button[contains(text(), 'Sign in to your business account')]"
        ]
    }
}

def example_usage():
    """
    Example of how to use the Amazon login automation.
    This is for educational purposes only.
    """
    
    # Initialize the automation
    amazon_login = AmazonLoginAutomation(headless=False)
    
    try:
        # Navigate to Amazon login
        amazon_login.navigate_to_login()
        
        # Enter credentials (replace with actual values)
        email = "your_email@example.com"
        password = "your_password"
        
        # Perform login
        amazon_login.enter_email(email)
        amazon_login.enter_password(password)
        
        # Check for 2FA
        if amazon_login.check_for_captcha():
            print("CAPTCHA detected - manual intervention required")
            input("Please solve CAPTCHA and press Enter...")
        
        # Check if logged in
        if amazon_login.is_logged_in():
            print("Successfully logged in!")
        else:
            error_msg = amazon_login.get_error_message()
            print(f"Login failed: {error_msg}")
    
    finally:
        # Clean up
        amazon_login.close()

if __name__ == "__main__":
    print("Amazon Login XPath Guide")
    print("========================")
    print()
    print("Available XPath selectors:")
    
    for element, xpath in vars(AmazonLoginXPaths).items():
        if not element.startswith('_'):
            print(f"{element}: {xpath}")
    
    print()
    print("IMPORTANT NOTES:")
    print("- Amazon frequently changes their UI, so XPaths may need updating")
    print("- Amazon has strict anti-bot measures as of late 2024")
    print("- Always respect Amazon's Terms of Service")
    print("- Use proxy rotation and delays to avoid detection")
    print("- Consider using Amazon's official APIs instead of scraping")
    
    # Uncomment to run example
    # example_usage()