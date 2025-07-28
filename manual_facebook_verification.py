"""
Manual Facebook Account Verification Guide
This script provides methods to manually verify if you're logged into your own Facebook account.
"""

import json
import time
from datetime import datetime

def print_manual_verification_steps():
    """Print step-by-step manual verification guide"""
    
    print("🔍 MANUAL FACEBOOK ACCOUNT VERIFICATION GUIDE")
    print("=" * 60)
    
    print("\n📋 STEP-BY-STEP VERIFICATION PROCESS:")
    print("-" * 40)
    
    steps = [
        {
            "step": "1. Check Login Status",
            "actions": [
                "Open Facebook.com in your browser",
                "If you see a login form, you're not logged in",
                "If you see the main Facebook interface, you're logged in"
            ]
        },
        {
            "step": "2. Verify Profile Name",
            "actions": [
                "Look at the top-right corner of Facebook",
                "Click on your profile picture or name",
                "Verify the name matches your real name",
                "Check if the profile picture is yours"
            ]
        },
        {
            "step": "3. Check Profile URL",
            "actions": [
                "Click on your profile picture to go to your profile",
                "Look at the URL in the address bar",
                "It should be facebook.com/your.name or facebook.com/profile.php?id=NUMBERS",
                "Save this URL for reference"
            ]
        },
        {
            "step": "4. Verify Account Settings",
            "actions": [
                "Click Settings & Privacy → Settings",
                "Go to 'Contact' section",
                "Check if the email address is yours",
                "Check if the phone number is yours",
                "Verify your birthday and other personal info"
            ]
        },
        {
            "step": "5. Check Recent Activity",
            "actions": [
                "Look at your timeline/news feed",
                "Check recent posts - are they yours?",
                "Check messages - do you recognize the conversations?",
                "Look at recent notifications"
            ]
        },
        {
            "step": "6. Verify Friends List",
            "actions": [
                "Go to your Friends list",
                "Check if you recognize the people",
                "Look for close friends and family members",
                "Check mutual friends with people you know"
            ]
        }
    ]
    
    for step_info in steps:
        print(f"\n🔸 {step_info['step']}:")
        for action in step_info['actions']:
            print(f"   • {action}")

def print_verification_checklist():
    """Print checklist of what to verify"""
    
    print("\n" + "=" * 60)
    print("✅ VERIFICATION CHECKLIST")
    print("=" * 60)
    
    print("\n🟢 POSITIVE INDICATORS (Your Account):")
    positive_indicators = [
        "Your real name appears in profile",
        "Your photo is the profile picture",
        "Your email/phone in account settings",
        "Your birthday and personal details",
        "Friends and family in friends list",
        "Your posts and photos on timeline",
        "Your writing style in posts/comments",
        "Familiar conversations in messages",
        "Your location/timezone settings",
        "Apps you remember connecting"
    ]
    
    for indicator in positive_indicators:
        print(f"   ✅ {indicator}")
    
    print("\n🔴 WARNING SIGNS (Not Your Account):")
    warning_signs = [
        "Unknown name in profile",
        "Unfamiliar profile picture",
        "Different email/phone in settings",
        "Wrong birthday or personal info",
        "Unknown people in friends list",
        "Posts in different language",
        "Unfamiliar photos and posts",
        "Messages with strangers",
        "Wrong location/timezone",
        "Unknown connected apps"
    ]
    
    for sign in warning_signs:
        print(f"   ❌ {sign}")

def print_url_analysis_guide():
    """Guide for analyzing Facebook URLs"""
    
    print("\n" + "=" * 60)
    print("🔗 FACEBOOK URL ANALYSIS GUIDE")
    print("=" * 60)
    
    print("\n📍 Common Facebook URL Patterns:")
    
    url_patterns = [
        {
            "pattern": "facebook.com/your.name",
            "description": "Custom username URL",
            "example": "facebook.com/john.doe.123",
            "note": "If you set a custom username, this is what you'll see"
        },
        {
            "pattern": "facebook.com/profile.php?id=NUMBERS",
            "description": "Numeric profile ID URL",
            "example": "facebook.com/profile.php?id=100012345678901",
            "note": "Default URL format with your unique Facebook ID"
        },
        {
            "pattern": "facebook.com/people/Name/ID",
            "description": "People directory URL",
            "example": "facebook.com/people/John-Doe/100012345678901",
            "note": "Alternative URL format sometimes used"
        }
    ]
    
    for pattern_info in url_patterns:
        print(f"\n🔸 {pattern_info['pattern']}")
        print(f"   Description: {pattern_info['description']}")
        print(f"   Example: {pattern_info['example']}")
        print(f"   Note: {pattern_info['note']}")
    
    print(f"\n💡 How to check your URL:")
    print(f"   1. Go to your Facebook profile")
    print(f"   2. Copy the URL from your browser's address bar")
    print(f"   3. The numbers after 'id=' are your unique Facebook profile ID")
    print(f"   4. Save this ID - it never changes and uniquely identifies your account")

def interactive_verification():
    """Interactive verification helper"""
    
    print("\n" + "=" * 60)
    print("🎯 INTERACTIVE ACCOUNT VERIFICATION")
    print("=" * 60)
    
    verification_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "verification_results": {}
    }
    
    questions = [
        {
            "key": "profile_name",
            "question": "What name is displayed on the Facebook profile?",
            "follow_up": "Is this your real name? (y/n)"
        },
        {
            "key": "profile_url",
            "question": "What is the profile URL? (copy from address bar)",
            "follow_up": "Does this URL look familiar to you? (y/n)"
        },
        {
            "key": "email_address",
            "question": "What email is shown in Settings → Contact?",
            "follow_up": "Is this your email address? (y/n)"
        },
        {
            "key": "friends_count",
            "question": "Approximately how many friends does the account have?",
            "follow_up": "Does this number seem right for your account? (y/n)"
        },
        {
            "key": "recent_posts",
            "question": "Look at the recent posts. What do you see?",
            "follow_up": "Are these posts made by you? (y/n)"
        }
    ]
    
    print("\n📋 Please answer the following questions by looking at Facebook:")
    print("(Press Enter to skip any question)")
    
    for q in questions:
        print(f"\n❓ {q['question']}")
        answer = input("   Your answer: ").strip()
        
        if answer:
            verification_data["verification_results"][q["key"]] = answer
            
            follow_up_answer = input(f"   {q['follow_up']} ").strip().lower()
            verification_data["verification_results"][f"{q['key']}_verified"] = follow_up_answer == 'y'
    
    # Calculate verification score
    verified_count = sum(1 for key, value in verification_data["verification_results"].items() 
                        if key.endswith("_verified") and value)
    total_questions = len([key for key in verification_data["verification_results"].keys() 
                          if key.endswith("_verified")])
    
    if total_questions > 0:
        verification_score = (verified_count / total_questions) * 100
        verification_data["verification_score"] = verification_score
        
        print(f"\n📊 VERIFICATION RESULTS:")
        print(f"   Verified answers: {verified_count}/{total_questions}")
        print(f"   Verification score: {verification_score:.1f}%")
        
        if verification_score >= 80:
            print("   🎉 HIGH CONFIDENCE: This appears to be your account!")
        elif verification_score >= 60:
            print("   ⚠️ MEDIUM CONFIDENCE: Some concerns, double-check details")
        else:
            print("   🚨 LOW CONFIDENCE: This may NOT be your account!")
    
    # Save verification data
    try:
        with open("facebook_verification_results.json", "w") as f:
            json.dump(verification_data, f, indent=2)
        print(f"\n💾 Verification results saved to facebook_verification_results.json")
    except Exception as e:
        print(f"⚠️ Could not save results: {e}")
    
    return verification_data

def print_browser_console_commands():
    """Print JavaScript commands to run in browser console"""
    
    print("\n" + "=" * 60)
    print("💻 BROWSER CONSOLE COMMANDS")
    print("=" * 60)
    
    print("\n🔧 Advanced users can run these JavaScript commands in browser console:")
    print("(Press F12 → Console tab on Facebook, then paste these commands)")
    
    commands = [
        {
            "purpose": "Get current user ID",
            "command": 'console.log("User ID:", require("CurrentUserInitialData").USER_ID);',
            "description": "Shows your Facebook user ID number"
        },
        {
            "purpose": "Get profile name",
            "command": 'console.log("Profile name:", document.title);',
            "description": "Shows the page title (usually contains your name)"
        },
        {
            "purpose": "Get current URL",
            "command": 'console.log("Current URL:", window.location.href);',
            "description": "Shows the current page URL"
        },
        {
            "purpose": "Check if logged in",
            "command": 'console.log("Logged in:", !!require("CurrentUserInitialData").USER_ID);',
            "description": "Returns true if logged in, false if not"
        }
    ]
    
    for cmd in commands:
        print(f"\n🔸 {cmd['purpose']}:")
        print(f"   Command: {cmd['command']}")
        print(f"   Purpose: {cmd['description']}")
    
    print(f"\n⚠️ Note: These commands may not work if Facebook changes their internal structure.")

def save_verification_template():
    """Save a template file for manual verification"""
    
    template_content = """
FACEBOOK ACCOUNT VERIFICATION CHECKLIST
=======================================

Date: _______________
Time: _______________

BASIC INFORMATION:
□ Profile Name: _________________________________
□ Profile URL: __________________________________
□ Email in Settings: ____________________________
□ Phone in Settings: ____________________________

VERIFICATION CHECKS:
□ Profile name matches my real name: Yes / No
□ Profile picture is mine: Yes / No
□ Email in settings is mine: Yes / No
□ Phone in settings is mine: Yes / No
□ Birthday in settings is correct: Yes / No
□ Friends list contains people I know: Yes / No
□ Recent posts are mine: Yes / No
□ Messages are familiar: Yes / No
□ Location/timezone is correct: Yes / No

SECURITY CHECKS:
□ Recent login activity looks normal: Yes / No
□ No suspicious apps connected: Yes / No
□ Two-factor authentication is set up: Yes / No
□ Recent security notifications: Yes / No

OVERALL ASSESSMENT:
□ This is definitely my account: Yes / No
□ Confidence level (1-10): ______

NOTES:
_________________________________________________
_________________________________________________
_________________________________________________

If you answered "No" to multiple questions above,
this may NOT be your Facebook account!
"""
    
    try:
        with open("facebook_verification_checklist.txt", "w") as f:
            f.write(template_content)
        print(f"📄 Verification checklist template saved to facebook_verification_checklist.txt")
        print(f"   You can print this and fill it out manually while checking Facebook.")
    except Exception as e:
        print(f"⚠️ Could not save template: {e}")

def main():
    """Main function with menu options"""
    
    print("🔍 FACEBOOK ACCOUNT VERIFICATION TOOLKIT")
    print("=" * 50)
    
    options = [
        ("1", "Show manual verification steps", print_manual_verification_steps),
        ("2", "Show verification checklist", print_verification_checklist),
        ("3", "URL analysis guide", print_url_analysis_guide),
        ("4", "Interactive verification", interactive_verification),
        ("5", "Browser console commands", print_browser_console_commands),
        ("6", "Save verification template", save_verification_template),
        ("7", "Show all information", lambda: [func() for _, _, func in options[:-2]])
    ]
    
    print("\nChoose an option:")
    for option, description, _ in options:
        print(f"   {option}. {description}")
    
    choice = input("\nEnter your choice (1-7): ").strip()
    
    for option, description, func in options:
        if choice == option:
            print(f"\n{description.upper()}:")
            func()
            return
    
    print("Invalid choice. Showing all information:")
    for _, _, func in options[:-2]:  # Exclude "Show all" option
        func()

if __name__ == "__main__":
    main()