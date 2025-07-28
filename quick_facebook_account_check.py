"""
Quick Facebook Account Check
A simplified script to quickly identify if you're logged into your own Facebook account.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import re

def setup_quick_driver():
    """Setup a Chrome driver quickly"""
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    try:
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print(f"Error setting up driver: {e}")
        return None

def quick_login_check(driver):
    """Quick check if user is logged into Facebook"""
    try:
        # Navigate to Facebook
        driver.get("https://www.facebook.com")
        time.sleep(3)
        
        # Check for login form (means not logged in)
        try:
            email_field = driver.find_element(By.XPATH, "//input[@id='email']")
            password_field = driver.find_element(By.XPATH, "//input[@id='pass']")
            if email_field and password_field:
                return False, "Found login form - not logged in"
        except NoSuchElementException:
            pass
        
        # Check for logged-in indicators
        logged_in_indicators = [
            ("Navigation bar", "//div[@role='banner']"),
            ("Main content", "//div[@role='main']"),
            ("Facebook logo", "//a[@aria-label='Facebook']"),
            ("Profile menu", "//div[@aria-label='Account']")
        ]
        
        for name, xpath in logged_in_indicators:
            try:
                element = driver.find_element(By.XPATH, xpath)
                if element:
                    return True, f"Found {name} - logged in"
            except NoSuchElementException:
                continue
        
        return None, "Login status unclear"
        
    except Exception as e:
        return None, f"Error checking login: {e}"

def get_basic_profile_info(driver):
    """Get basic profile information"""
    info = {}
    
    # Get current page title
    info['page_title'] = driver.title
    info['current_url'] = driver.current_url
    
    # Try to get profile name from various sources
    name_sources = [
        ("Page title", lambda: driver.title),
        ("Navigation", "//div[@role='banner']//span[string-length(text()) > 2]"),
        ("Profile link", "//a[contains(@href, '/me')]"),
        ("Account menu", "//div[@aria-label='Account']//span")
    ]
    
    for source_name, source in name_sources:
        try:
            if callable(source):
                text = source()
                # Extract name from title like "Facebook - John Doe"
                if ' - ' in text:
                    potential_name = text.split(' - ')[-1].strip()
                    if len(potential_name) > 1 and not potential_name.lower().startswith('facebook'):
                        info['name'] = potential_name
                        info['name_source'] = source_name
                        break
            else:
                elements = driver.find_elements(By.XPATH, source)
                for element in elements:
                    text = element.text.strip()
                    if text and len(text) > 1 and not text.isdigit():
                        excluded = ['Menu', 'Home', 'Search', 'Notifications', 'Settings', 'Facebook']
                        if text not in excluded:
                            info['name'] = text
                            info['name_source'] = source_name
                            break
                if 'name' in info:
                    break
        except Exception:
            continue
    
    return info

def get_profile_id_quick(driver):
    """Quick method to get profile ID"""
    try:
        # Navigate to profile
        driver.get("https://www.facebook.com/me")
        time.sleep(2)
        
        current_url = driver.current_url
        
        # Try to extract ID from URL
        id_patterns = [
            r'facebook\.com/profile\.php\?id=(\d+)',
            r'facebook\.com/(\d+)',
            r'id=(\d+)'
        ]
        
        for pattern in id_patterns:
            match = re.search(pattern, current_url)
            if match:
                return match.group(1)
        
        # If URL doesn't contain ID, try page source
        page_source = driver.page_source
        source_patterns = [
            r'"userID":"(\d+)"',
            r'"USER_ID":"(\d+)"'
        ]
        
        for pattern in source_patterns:
            matches = re.findall(pattern, page_source)
            if matches:
                return matches[0]
                
    except Exception as e:
        print(f"Error getting profile ID: {e}")
    
    return None

def quick_account_check():
    """Main function for quick account checking"""
    print("🚀 Quick Facebook Account Check")
    print("=" * 40)
    
    # Setup driver
    driver = setup_quick_driver()
    if not driver:
        print("❌ Could not setup browser driver")
        return
    
    try:
        # Check login status
        print("🔍 Checking login status...")
        is_logged_in, login_message = quick_login_check(driver)
        print(f"   {login_message}")
        
        if not is_logged_in:
            print("\n❌ Not logged in to Facebook")
            print("Please log in manually and run the script again.")
            return
        
        print("\n✅ Logged in! Collecting basic account info...")
        
        # Get basic profile info
        profile_info = get_basic_profile_info(driver)
        
        # Get profile ID
        print("🆔 Getting profile ID...")
        profile_id = get_profile_id_quick(driver)
        
        # Print results
        print("\n" + "=" * 40)
        print("📊 ACCOUNT INFORMATION")
        print("=" * 40)
        
        print(f"🌐 Current URL: {profile_info.get('current_url', 'Unknown')}")
        print(f"📄 Page Title: {profile_info.get('page_title', 'Unknown')}")
        
        if 'name' in profile_info:
            print(f"📝 Profile Name: {profile_info['name']}")
            print(f"   (Found via: {profile_info.get('name_source', 'Unknown')})")
        else:
            print("📝 Profile Name: Not found")
        
        if profile_id:
            print(f"🆔 Profile ID: {profile_id}")
        else:
            print("🆔 Profile ID: Not found")
        
        print("=" * 40)
        
        # Quick verification prompt
        if 'name' in profile_info:
            print(f"\n🔍 VERIFICATION:")
            user_name = input(f"Is '{profile_info['name']}' your name? (y/n): ").strip().lower()
            
            if user_name == 'y':
                print("✅ Great! This appears to be your Facebook account.")
            else:
                print("⚠️ WARNING: This may not be your account!")
                print("   Please verify you're logged into the correct Facebook account.")
        
        # Save basic info to file
        try:
            with open("facebook_account_check.txt", "w") as f:
                f.write("Facebook Account Check Results\n")
                f.write("=" * 40 + "\n")
                f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"URL: {profile_info.get('current_url', 'Unknown')}\n")
                f.write(f"Page Title: {profile_info.get('page_title', 'Unknown')}\n")
                f.write(f"Profile Name: {profile_info.get('name', 'Not found')}\n")
                f.write(f"Profile ID: {profile_id or 'Not found'}\n")
            
            print(f"\n💾 Results saved to facebook_account_check.txt")
            
        except Exception as e:
            print(f"⚠️ Could not save results: {e}")
        
    except Exception as e:
        print(f"❌ Error during check: {e}")
    
    finally:
        print(f"\nClosing browser in 5 seconds...")
        time.sleep(5)
        driver.quit()

def manual_verification_helper():
    """Helper function to manually verify account without automation"""
    print("🔍 Manual Facebook Account Verification Helper")
    print("=" * 50)
    print("\nTo manually verify your Facebook account:")
    
    steps = [
        "1. Open Facebook in your browser",
        "2. Make sure you're logged in",
        "3. Click on your profile picture or name (top right)",
        "4. Look at the URL - it should contain your profile ID or username",
        "5. Check the page title - it should show your name",
        "6. Verify the profile information matches your details"
    ]
    
    for step in steps:
        print(f"   {step}")
    
    print("\n🔍 What to look for:")
    verification_points = [
        "✓ Profile name matches your real name",
        "✓ Profile picture is yours",
        "✓ Friends list contains people you know",
        "✓ Timeline posts are yours",
        "✓ Account creation date makes sense",
        "✓ Email/phone in settings matches yours"
    ]
    
    for point in verification_points:
        print(f"   {point}")
    
    print("\n⚠️ Red flags (signs it's NOT your account):")
    red_flags = [
        "✗ Unknown profile name",
        "✗ Unfamiliar profile picture", 
        "✗ Friends you don't recognize",
        "✗ Posts in a different language",
        "✗ Different location/timezone",
        "✗ Unknown email/phone in settings"
    ]
    
    for flag in red_flags:
        print(f"   {flag}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--manual":
        manual_verification_helper()
    else:
        print("Quick Facebook Account Check")
        print("Use --manual flag for manual verification steps")
        print()
        quick_account_check()