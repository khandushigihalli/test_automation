"""
Configuration file for Selenium automation framework
"""

import os
from enum import Enum


class Environment(Enum):
    """Environment enumeration"""
    DEV = "development"
    TEST = "testing"
    PROD = "production"


class Config:
    """Base configuration class"""
    
    # Browser settings
    DEFAULT_BROWSER = "chrome"
    HEADLESS_MODE = False
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    PAGE_LOAD_TIMEOUT = 30
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_PATH = "screenshots/"
    
    # Logging settings
    LOG_LEVEL = "INFO"
    LOG_FILE = "selenium_tests.log"
    
    # Test data
    TEST_DATA_PATH = "test_data/"
    
    # Report settings
    REPORT_PATH = "reports/"
    
    @staticmethod
    def get_base_url(environment=Environment.DEV):
        """Get base URL based on environment"""
        urls = {
            Environment.DEV: "http://35.154.213.24",
            Environment.TEST: "http://test.example.com",
            Environment.PROD: "http://prod.example.com"
        }
        return urls.get(environment, urls[Environment.DEV])
    
    @staticmethod
    def get_test_credentials():
        """Get test credentials"""
        return {
            "valid_user": {
                "username": "9108668521",
                "password": "khan8521"
            },
            "invalid_users": [
                {"username": "invalid", "password": "invalid"},
                {"username": "", "password": ""},
                {"username": "1234567890", "password": "wrongpass"}
            ]
        }
    
    @staticmethod
    def create_directories():
        """Create necessary directories if they don't exist"""
        directories = [
            Config.SCREENSHOT_PATH,
            Config.TEST_DATA_PATH,
            Config.REPORT_PATH
        ]
        
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")


# Browser capabilities
CHROME_OPTIONS = [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-extensions",
    "--window-size=1920,1080"
]

FIREFOX_OPTIONS = [
    "--width=1920",
    "--height=1080"
]

# Element locator strategies
class LocatorStrategy:
    """Common locator strategies"""
    ID = "id"
    NAME = "name"
    CLASS_NAME = "class name"
    TAG_NAME = "tag name"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    CSS_SELECTOR = "css selector"
    XPATH = "xpath"


# Common test data
TEST_SEARCH_TERMS = [
    "Selenium WebDriver",
    "Python automation",
    "Test automation framework",
    "Web testing tools"
]

# Database configuration (if needed)
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "database": "test_db",
    "username": "test_user",
    "password": "test_password"
}

# API configuration (if needed)
API_CONFIG = {
    "base_url": "https://api.example.com",
    "timeout": 30,
    "headers": {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
}