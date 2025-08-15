"""
Facebook Account Identifier
This module helps identify if you're logged into your own Facebook account
by checking various profile indicators and account information.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import json
import re

class FacebookAccountIdentifier:
    """
    Class to identify and verify Facebook account ownership
    """
    
    def __init__(self, driver=None, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout) if driver else None
        self.account_info = {}
    
    def setup_driver(self, headless=False):
        """Setup Chrome WebDriver with appropriate options"""
        chrome_options = Options()
        
        if headless:
            chrome_options.add_argument("--headless")
        
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, self.timeout)
        return self.driver
    
    def check_login_status(self):
        """Check if user is logged into Facebook"""
        try:
            # Check for login indicators
            login_indicators = [
                "//div[@role='banner']",  # Top navigation bar
                "//div[@data-testid='blue_bar']",  # Blue navigation bar
                "//a[@aria-label='Facebook']",  # Facebook logo when logged in
                "//div[contains(@class, 'fb_content')]",  # Facebook content area
                "//div[@role='main']"  # Main content area
            ]
            
            for indicator in login_indicators:
                try:
                    element = self.driver.find_element(By.XPATH, indicator)
                    if element:
                        print("✓ User appears to be logged in")
                        return True
                except NoSuchElementException:
                    continue
            
            # Check if we're on login page
            login_page_indicators = [
                "//input[@id='email']",
                "//input[@id='pass']",
                "//button[@name='login']"
            ]
            
            login_elements_found = 0
            for indicator in login_page_indicators:
                try:
                    self.driver.find_element(By.XPATH, indicator)
                    login_elements_found += 1
                except NoSuchElementException:
                    continue
            
            if login_elements_found >= 2:
                print("✗ User is not logged in (on login page)")
                return False
            
            print("? Login status unclear")
            return None
            
        except Exception as e:
            print(f"Error checking login status: {e}")
            return None
    
    def get_profile_name(self):
        """Extract the profile name from various locations"""
        name_xpaths = [
            # Profile dropdown menu
            "//div[@aria-label='Account']//span",
            "//div[@role='button']//span[contains(@class, 'x1lliihq')]",
            
            # Navigation area name
            "//div[@role='banner']//span[contains(text(), ' ')]",
            "//div[@data-testid='blue_bar']//span",
            
            # Profile page title
            "//h1",
            "//title",
            
            # Settings page name
            "//div[contains(@class, 'x1i10hfl')]//span",
            
            # Alternative profile indicators
            "//a[contains(@href, '/me')]//span",
            "//div[@role='main']//h1",
            "//span[contains(@dir, 'auto') and string-length(text()) > 2]"
        ]
        
        for xpath in name_xpaths:
            try:
                elements = self.driver.find_elements(By.XPATH, xpath)
                for element in elements:
                    text = element.text.strip()
                    if text and len(text) > 1 and not text.isdigit():
                        # Filter out common non-name texts
                        excluded_texts = ['Menu', 'Home', 'Search', 'Messenger', 'Create', 'Notifications', 'Account', 'Settings']
                        if text not in excluded_texts and not text.startswith('http'):
                            print(f"Found potential name: {text} (using {xpath})")
                            return text
            except Exception as e:
                continue
        
        return None
    
    def get_profile_email(self):
        """Get profile email from settings or account info"""
        try:
            # Navigate to settings
            self.driver.get("https://www.facebook.com/settings")
            time.sleep(3)
            
            email_xpaths = [
                "//div[contains(text(), '@')]",
                "//span[contains(text(), '@')]",
                "//input[@type='email']/@value",
                "//div[@role='main']//div[contains(text(), '@')]"
            ]
            
            for xpath in email_xpaths:
                try:
                    elements = self.driver.find_elements(By.XPATH, xpath)
                    for element in elements:
                        text = element.text.strip()
                        if '@' in text and '.' in text:
                            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                            matches = re.findall(email_pattern, text)
                            if matches:
                                return matches[0]
                except Exception:
                    continue
            
        except Exception as e:
            print(f"Error getting email: {e}")
        
        return None
    
    def get_profile_id(self):
        """Extract Facebook profile ID"""
        try:
            # Method 1: From URL when visiting profile
            self.driver.get("https://www.facebook.com/me")
            time.sleep(2)
            
            current_url = self.driver.current_url
            
            # Extract ID from URL patterns
            patterns = [
                r'facebook\.com/profile\.php\?id=(\d+)',
                r'facebook\.com/(\d+)',
                r'id=(\d+)'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, current_url)
                if match:
                    return match.group(1)
            
            # Method 2: From page source
            page_source = self.driver.page_source
            id_patterns = [
                r'"userID":"(\d+)"',
                r'"USER_ID":"(\d+)"',
                r'"id":"(\d+)"',
                r'profile_id=(\d+)'
            ]
            
            for pattern in id_patterns:
                matches = re.findall(pattern, page_source)
                if matches:
                    return matches[0]
            
        except Exception as e:
            print(f"Error getting profile ID: {e}")
        
        return None
    
    def get_profile_picture_url(self):
        """Get profile picture URL"""
        try:
            profile_pic_xpaths = [
                "//img[contains(@alt, 'profile picture') or contains(@data-testid, 'profile-picture')]/@src",
                "//div[@role='img']//img/@src",
                "//img[contains(@src, 'profile')]/@src"
            ]
            
            for xpath in profile_pic_xpaths:
                try:
                    elements = self.driver.find_elements(By.XPATH, xpath)
                    for element in elements:
                        src = element.get_attribute('src')
                        if src and 'profile' in src.lower():
                            return src
                except Exception:
                    continue
                    
        except Exception as e:
            print(f"Error getting profile picture: {e}")
        
        return None
    
    def get_friends_count(self):
        """Get approximate friends count"""
        try:
            # Navigate to friends page
            self.driver.get("https://www.facebook.com/me/friends")
            time.sleep(3)
            
            friends_count_xpaths = [
                "//span[contains(text(), 'friends')]",
                "//div[contains(text(), 'friends')]",
                "//h2[contains(text(), 'Friends')]",
            ]
            
            for xpath in friends_count_xpaths:
                try:
                    elements = self.driver.find_elements(By.XPATH, xpath)
                    for element in elements:
                        text = element.text
                        numbers = re.findall(r'\d+', text)
                        if numbers:
                            return int(numbers[0])
                except Exception:
                    continue
                    
        except Exception as e:
            print(f"Error getting friends count: {e}")
        
        return None
    
    def collect_account_info(self):
        """Collect all available account information"""
        print("🔍 Collecting account information...")
        
        # Check login status first
        is_logged_in = self.check_login_status()
        if not is_logged_in:
            print("❌ Not logged in to Facebook")
            return None
        
        self.account_info = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'is_logged_in': is_logged_in
        }
        
        # Collect profile information
        print("📝 Getting profile name...")
        self.account_info['name'] = self.get_profile_name()
        
        print("📧 Getting profile email...")
        self.account_info['email'] = self.get_profile_email()
        
        print("🆔 Getting profile ID...")
        self.account_info['profile_id'] = self.get_profile_id()
        
        print("🖼️ Getting profile picture...")
        self.account_info['profile_picture'] = self.get_profile_picture_url()
        
        print("👥 Getting friends count...")
        self.account_info['friends_count'] = self.get_friends_count()
        
        # Additional browser/session info
        self.account_info['current_url'] = self.driver.current_url
        self.account_info['page_title'] = self.driver.title
        
        return self.account_info
    
    def verify_account_ownership(self, expected_info):
        """
        Verify if the current account matches expected account information
        
        Args:
            expected_info (dict): Dictionary with expected account information
                - name: Expected profile name
                - email: Expected email address
                - profile_id: Expected profile ID
                - friends_count_range: Tuple of (min, max) expected friends count
        """
        if not self.account_info:
            print("❌ No account information collected. Run collect_account_info() first.")
            return False
        
        verification_results = {}
        overall_match = True
        
        print("\n🔍 Verifying account ownership...")
        print("=" * 50)
        
        # Check name
        if 'name' in expected_info and expected_info['name']:
            current_name = self.account_info.get('name', '').lower()
            expected_name = expected_info['name'].lower()
            
            name_match = expected_name in current_name or current_name in expected_name
            verification_results['name_match'] = name_match
            
            print(f"📝 Name verification:")
            print(f"   Expected: {expected_info['name']}")
            print(f"   Found: {self.account_info.get('name', 'Not found')}")
            print(f"   Match: {'✅' if name_match else '❌'}")
            
            if not name_match:
                overall_match = False
        
        # Check email
        if 'email' in expected_info and expected_info['email']:
            current_email = self.account_info.get('email', '').lower()
            expected_email = expected_info['email'].lower()
            
            email_match = current_email == expected_email
            verification_results['email_match'] = email_match
            
            print(f"\n📧 Email verification:")
            print(f"   Expected: {expected_info['email']}")
            print(f"   Found: {self.account_info.get('email', 'Not found')}")
            print(f"   Match: {'✅' if email_match else '❌'}")
            
            if not email_match:
                overall_match = False
        
        # Check profile ID
        if 'profile_id' in expected_info and expected_info['profile_id']:
            current_id = self.account_info.get('profile_id', '')
            expected_id = str(expected_info['profile_id'])
            
            id_match = current_id == expected_id
            verification_results['id_match'] = id_match
            
            print(f"\n🆔 Profile ID verification:")
            print(f"   Expected: {expected_id}")
            print(f"   Found: {current_id or 'Not found'}")
            print(f"   Match: {'✅' if id_match else '❌'}")
            
            if not id_match:
                overall_match = False
        
        # Check friends count range
        if 'friends_count_range' in expected_info and expected_info['friends_count_range']:
            current_count = self.account_info.get('friends_count')
            min_count, max_count = expected_info['friends_count_range']
            
            count_match = current_count and min_count <= current_count <= max_count
            verification_results['friends_count_match'] = count_match
            
            print(f"\n👥 Friends count verification:")
            print(f"   Expected range: {min_count} - {max_count}")
            print(f"   Found: {current_count or 'Not found'}")
            print(f"   Match: {'✅' if count_match else '❌'}")
            
            if not count_match:
                overall_match = False
        
        print("\n" + "=" * 50)
        print(f"🎯 Overall verification: {'✅ VERIFIED - This is your account!' if overall_match else '❌ NOT VERIFIED - This may not be your account'}")
        
        return overall_match, verification_results
    
    def save_account_fingerprint(self, filename="my_facebook_account.json"):
        """Save account information as a fingerprint for future verification"""
        if not self.account_info:
            print("❌ No account information to save")
            return False
        
        try:
            with open(filename, 'w') as f:
                json.dump(self.account_info, f, indent=2)
            print(f"💾 Account fingerprint saved to {filename}")
            return True
        except Exception as e:
            print(f"❌ Error saving fingerprint: {e}")
            return False
    
    def load_account_fingerprint(self, filename="my_facebook_account.json"):
        """Load saved account fingerprint"""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Error loading fingerprint: {e}")
            return None
    
    def print_account_summary(self):
        """Print a summary of collected account information"""
        if not self.account_info:
            print("❌ No account information available")
            return
        
        print("\n" + "=" * 60)
        print("📊 FACEBOOK ACCOUNT SUMMARY")
        print("=" * 60)
        
        info_items = [
            ("🔐 Login Status", "✅ Logged In" if self.account_info.get('is_logged_in') else "❌ Not Logged In"),
            ("📝 Profile Name", self.account_info.get('name', 'Not found')),
            ("📧 Email Address", self.account_info.get('email', 'Not found')),
            ("🆔 Profile ID", self.account_info.get('profile_id', 'Not found')),
            ("👥 Friends Count", self.account_info.get('friends_count', 'Not found')),
            ("🌐 Current URL", self.account_info.get('current_url', 'Not found')),
            ("📄 Page Title", self.account_info.get('page_title', 'Not found')),
            ("⏰ Collected At", self.account_info.get('timestamp', 'Not found'))
        ]
        
        for label, value in info_items:
            print(f"{label:<20} {value}")
        
        print("=" * 60)

def example_usage():
    """Example of how to use the FacebookAccountIdentifier"""
    
    print("🚀 Facebook Account Identifier - Example Usage")
    print("=" * 60)
    
    # Initialize the identifier
    identifier = FacebookAccountIdentifier()
    
    try:
        # Setup driver
        driver = identifier.setup_driver(headless=False)
        
        print("📱 Please manually log into Facebook in the opened browser...")
        print("Press Enter when you're logged in...")
        input()
        
        # Collect account information
        account_info = identifier.collect_account_info()
        
        if account_info:
            # Print summary
            identifier.print_account_summary()
            
            # Save fingerprint
            identifier.save_account_fingerprint()
            
            # Example verification against expected information
            expected_info = {
                'name': input("\n🔍 Enter your expected name for verification: ").strip(),
                'email': input("🔍 Enter your expected email for verification: ").strip(),
                # 'profile_id': '123456789',  # Uncomment and set if known
                # 'friends_count_range': (50, 500)  # Uncomment and set if known
            }
            
            if expected_info['name'] or expected_info['email']:
                is_verified, results = identifier.verify_account_ownership(expected_info)
                
                if is_verified:
                    print("\n🎉 SUCCESS: This appears to be your Facebook account!")
                else:
                    print("\n⚠️ WARNING: This may not be your Facebook account!")
        
        input("\nPress Enter to close the browser...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        if hasattr(identifier, 'driver') and identifier.driver:
            identifier.driver.quit()

if __name__ == "__main__":
    example_usage()