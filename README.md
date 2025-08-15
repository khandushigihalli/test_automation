# Facebook Account Identification Tools

This repository contains Python tools to help you identify if you're logged into your own Facebook account. The tools use various methods from automated browser checking to manual verification guides.

## 📁 Files Overview

### 1. `facebook_account_identifier.py` - Complete Automation Solution
**Full-featured script with Selenium WebDriver automation**

- ✅ Automated login status checking
- ✅ Profile name extraction 
- ✅ Email address detection
- ✅ Profile ID extraction
- ✅ Friends count analysis
- ✅ Account verification against expected information
- ✅ Account fingerprinting (save/load account info)

**Usage:**
```python
from facebook_account_identifier import FacebookAccountIdentifier

identifier = FacebookAccountIdentifier()
driver = identifier.setup_driver()
account_info = identifier.collect_account_info()
identifier.print_account_summary()
```

### 2. `quick_facebook_account_check.py` - Simplified Automation
**Lightweight script for quick account verification**

- ✅ Quick login status check
- ✅ Basic profile information extraction
- ✅ Profile ID detection
- ✅ Simple verification prompts
- ✅ Results saving

**Usage:**
```bash
python3 quick_facebook_account_check.py
```

### 3. `manual_facebook_verification.py` - Manual Verification Guide
**No automation required - step-by-step manual verification**

- ✅ Interactive verification toolkit
- ✅ Comprehensive verification checklist
- ✅ URL analysis guide
- ✅ Browser console commands
- ✅ Printable verification template

**Usage:**
```bash
python3 manual_facebook_verification.py
```

### 4. `facebook_login_xpath.py` & `simple_xpath_demo.py` - XPath References
**XPath expressions for Facebook login elements**

- ✅ Comprehensive XPath expressions for all Facebook login elements
- ✅ Multiple fallback XPaths for reliability
- ✅ Usage examples for different automation tools

## 🚀 Quick Start

### Method 1: Automated Account Check (Requires Selenium)
```bash
# Install dependencies
pip install selenium webdriver-manager

# Run automated check
python3 facebook_account_identifier.py
```

### Method 2: Manual Verification (No dependencies)
```bash
# Run manual verification guide
python3 manual_facebook_verification.py
```

### Method 3: Quick Check (Requires Selenium)
```bash
# Run quick automated check
python3 quick_facebook_account_check.py
```

## 🔍 Key Verification Methods

### Automated Methods:
1. **Profile Name Detection** - Extract name from page title, navigation, profile links
2. **Profile ID Extraction** - Get unique Facebook profile ID from URL or page source
3. **Email Detection** - Extract email from account settings pages
4. **Login Status Check** - Verify if user is logged in by checking page elements
5. **Friends Count Analysis** - Get approximate friends count for verification

### Manual Verification Points:
1. **Profile Information** - Name, picture, email, phone match your details
2. **Friends List** - Contains people you know and recognize
3. **Timeline Content** - Posts, photos, and activity are yours
4. **Messages** - Conversations are familiar and with people you know
5. **Account Settings** - Email, phone, birthday, location are correct
6. **URL Analysis** - Profile URL contains your expected username or ID

## 📊 Verification Checklist

### ✅ Positive Indicators (Your Account):
- Your real name appears in profile
- Your photo is the profile picture  
- Your email/phone in account settings
- Friends and family in friends list
- Your posts and photos on timeline
- Familiar conversations in messages
- Your location/timezone settings

### ❌ Warning Signs (Not Your Account):
- Unknown name in profile
- Unfamiliar profile picture
- Different email/phone in settings
- Unknown people in friends list
- Posts in different language
- Messages with strangers
- Wrong location/timezone

## 🔗 Facebook URL Patterns

- **Custom Username:** `facebook.com/your.name`
- **Numeric ID:** `facebook.com/profile.php?id=123456789`
- **People Directory:** `facebook.com/people/Name/123456789`

## 💻 Browser Console Commands

For advanced users, run these in Facebook's browser console (F12):

```javascript
// Get your user ID
console.log("User ID:", require("CurrentUserInitialData").USER_ID);

// Check if logged in
console.log("Logged in:", !!require("CurrentUserInitialData").USER_ID);

// Get current URL
console.log("Current URL:", window.location.href);
```

## 🛡️ Security Notes

- **Privacy:** These tools only access information already visible to you
- **No Passwords:** Scripts never handle or store Facebook passwords
- **Local Only:** All data processing happens locally on your machine
- **Read-Only:** Tools only read information, never modify your account

## 📋 Requirements

### For Automated Tools:
- Python 3.6+
- Selenium WebDriver
- Chrome browser and ChromeDriver

```bash
pip install selenium webdriver-manager
```

### For Manual Tools:
- Python 3.6+ (no additional packages required)

## 🎯 Use Cases

1. **Account Security** - Verify you're logged into the correct account
2. **Shared Computers** - Ensure you're not using someone else's logged-in account
3. **Account Recovery** - Confirm account ownership during recovery process
4. **Automation Testing** - Verify correct account in automated scripts
5. **Multi-Account Management** - Distinguish between multiple accounts

## ⚠️ Important Notes

- Facebook's interface changes frequently - some XPath expressions may need updates
- Always respect Facebook's Terms of Service
- Use these tools responsibly and only on accounts you own
- Some methods may not work if Facebook implements new security measures

## 🔧 Troubleshooting

**Common Issues:**
1. **ChromeDriver not found** - Install using `pip install webdriver-manager`
2. **Element not found** - Facebook may have changed their HTML structure
3. **Login required** - Make sure you're logged into Facebook before running scripts
4. **Rate limiting** - Add delays between requests if Facebook blocks automation

## 📞 Support

If you encounter issues:
1. Check that you're logged into Facebook
2. Verify ChromeDriver is installed and up-to-date
3. Try the manual verification methods as fallback
4. Update the XPath expressions if Facebook changed their interface

---

**Remember:** These tools are designed to help you verify YOUR OWN Facebook account. Always use them responsibly and in accordance with Facebook's Terms of Service.