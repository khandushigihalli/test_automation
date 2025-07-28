#!/usr/bin/env python3
"""
Test Runner for Selenium Automation
This script provides an easy way to run different types of Selenium tests
"""

import sys
import argparse
import subprocess
from config import Config


def run_basic_examples():
    """Run basic Selenium examples"""
    print("Running basic Selenium examples...")
    try:
        result = subprocess.run([sys.executable, "selenium_examples.py"], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running basic examples: {e}")
        return False


def run_improved_framework():
    """Run improved framework tests"""
    print("Running improved framework tests...")
    try:
        result = subprocess.run([sys.executable, "improved_selenium_framework.py"], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running improved framework: {e}")
        return False


def run_pytest_tests():
    """Run tests using pytest"""
    print("Running tests with pytest...")
    try:
        # Create directories first
        Config.create_directories()
        
        # Run pytest with HTML report
        cmd = [
            sys.executable, "-m", "pytest", 
            "selenium_examples.py", 
            "-v", 
            "--html=reports/pytest_report.html", 
            "--self-contained-html"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running pytest: {e}")
        return False


def run_specific_test(test_name):
    """Run a specific test"""
    print(f"Running specific test: {test_name}")
    try:
        cmd = [sys.executable, "-m", "pytest", "selenium_examples.py", "-k", test_name, "-v"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running specific test: {e}")
        return False


def check_dependencies():
    """Check if required dependencies are installed"""
    print("Checking dependencies...")
    
    required_packages = [
        "selenium",
        "pytest",
        "webdriver-manager"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✓ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} is NOT installed")
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Please install them using:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("All dependencies are installed!")
    return True


def setup_environment():
    """Setup test environment"""
    print("Setting up test environment...")
    
    # Create necessary directories
    Config.create_directories()
    
    # Check Chrome/Chromedriver
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=options)
        driver.quit()
        print("✓ Chrome WebDriver is working")
        return True
    except Exception as e:
        print(f"✗ Chrome WebDriver setup failed: {e}")
        print("Please install ChromeDriver or use webdriver-manager")
        return False


def main():
    """Main function to parse arguments and run tests"""
    parser = argparse.ArgumentParser(description="Selenium Test Runner")
    parser.add_argument("--test-type", 
                       choices=["basic", "improved", "pytest", "specific"],
                       default="basic",
                       help="Type of test to run")
    parser.add_argument("--test-name", 
                       help="Specific test name to run (for specific test-type)")
    parser.add_argument("--check-deps", 
                       action="store_true",
                       help="Check if dependencies are installed")
    parser.add_argument("--setup", 
                       action="store_true",
                       help="Setup test environment")
    parser.add_argument("--headless", 
                       action="store_true",
                       help="Run tests in headless mode")
    
    args = parser.parse_args()
    
    if args.check_deps:
        success = check_dependencies()
        sys.exit(0 if success else 1)
    
    if args.setup:
        success = setup_environment()
        sys.exit(0 if success else 1)
    
    # Check dependencies before running tests
    if not check_dependencies():
        print("Please install missing dependencies first")
        sys.exit(1)
    
    # Setup environment
    if not setup_environment():
        print("Environment setup failed")
        sys.exit(1)
    
    # Set headless mode if specified
    if args.headless:
        import os
        os.environ["HEADLESS_MODE"] = "true"
    
    # Run the specified test type
    success = False
    
    if args.test_type == "basic":
        success = run_basic_examples()
    elif args.test_type == "improved":
        success = run_improved_framework()
    elif args.test_type == "pytest":
        success = run_pytest_tests()
    elif args.test_type == "specific":
        if args.test_name:
            success = run_specific_test(args.test_name)
        else:
            print("Please provide --test-name for specific test type")
            sys.exit(1)
    
    if success:
        print("\n✓ Tests completed successfully!")
        sys.exit(0)
    else:
        print("\n✗ Tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()