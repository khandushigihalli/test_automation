# Selenium Automation Framework

This repository contains a comprehensive Selenium WebDriver automation framework with examples, utilities, and best practices for web testing.

## 📁 Project Structure

```
├── selenium_examples.py           # Comprehensive Selenium examples
├── improved_selenium_framework.py # Enhanced framework with modern practices
├── config.py                     # Configuration settings
├── run_tests.py                  # Test runner script
├── selenium_requirements.txt     # Python dependencies
├── SELENIUM_README.md            # This documentation
└── screenshots/                  # Generated screenshots
└── reports/                      # Test reports
└── test_data/                    # Test data files
```

## 🚀 Features

### Basic Examples (`selenium_examples.py`)
- **Google Search Automation**: Automated search functionality
- **Form Handling**: Text input, dropdowns, checkboxes
- **Wait Strategies**: Explicit and implicit waits
- **JavaScript Execution**: Custom JavaScript in browser
- **Mouse Actions**: Hover, click, drag and drop
- **Window Handling**: Multiple tabs/windows
- **Screenshot Capture**: Full page and element screenshots
- **File Upload**: Automated file uploading

### Enhanced Framework (`improved_selenium_framework.py`)
- **Driver Management**: Optimized Chrome driver setup
- **Enhanced Base Page**: Robust element interactions
- **Error Handling**: Comprehensive exception handling
- **Logging**: Detailed test execution logs
- **Test Runner**: Automated test execution with reporting
- **Page Object Model**: Clean, maintainable test structure

## 🔧 Installation

### 1. Install Python Dependencies
```bash
pip install -r selenium_requirements.txt
```

### 2. Install Chrome Browser
Make sure you have Google Chrome installed on your system.

### 3. ChromeDriver (Optional)
The framework can auto-download ChromeDriver, but you can also install it manually:
- Download from: https://chromedriver.chromium.org/
- Add to PATH or place in project directory

## 🏃‍♂️ Quick Start

### Check Dependencies
```bash
python run_tests.py --check-deps
```

### Setup Environment
```bash
python run_tests.py --setup
```

### Run Basic Examples
```bash
python run_tests.py --test-type basic
```

### Run Improved Framework
```bash
python run_tests.py --test-type improved
```

### Run with Pytest
```bash
python run_tests.py --test-type pytest
```

### Run Specific Test
```bash
python run_tests.py --test-type specific --test-name "test_google_search"
```

### Run in Headless Mode
```bash
python run_tests.py --test-type basic --headless
```

## 📖 Usage Examples

### Basic Selenium Automation
```python
from selenium_examples import SeleniumExamples

# Initialize
examples = SeleniumExamples()
examples.setup_driver(headless=False)

try:
    # Run Google search
    examples.example_google_search("Selenium WebDriver")
    
    # Handle dropdowns
    examples.example_dropdown_handling()
    
    # Take screenshots
    examples.example_screenshot_capture()
    
finally:
    examples.teardown_driver()
```

### Using Enhanced Framework
```python
from improved_selenium_framework import SeleniumTestRunner

# Create test runner
runner = SeleniumTestRunner(headless=False)

# Setup and run tests
if runner.setup():
    runner.run_login_tests()
    runner.generate_report()
    runner.teardown()
```

### Page Object Model Example
```python
from improved_selenium_framework import ImprovedLoginPage, ImprovedDriverManager

# Setup driver
driver = ImprovedDriverManager.get_chrome_driver()

# Create page object
login_page = ImprovedLoginPage(driver)

# Use page methods
login_page.navigate_to_login()
login_page.login("username", "password")

# Cleanup
driver.quit()
```

## 🧪 Test Categories

### 1. Functional Tests
- Login/logout functionality
- Form submissions
- Navigation testing
- Data validation

### 2. UI Tests
- Element visibility
- Layout verification
- Responsive design
- Cross-browser compatibility

### 3. Integration Tests
- API + UI testing
- Database + UI testing
- End-to-end workflows

## 📊 Reporting

### Pytest HTML Reports
```bash
python -m pytest selenium_examples.py --html=reports/report.html --self-contained-html
```

### Custom Test Reports
The improved framework generates detailed test execution reports with:
- Test execution summary
- Pass/fail statistics
- Detailed logs
- Screenshots on failure

## 🔧 Configuration

### Browser Settings (`config.py`)
```python
# Modify browser settings
Config.DEFAULT_BROWSER = "chrome"  # or "firefox"
Config.HEADLESS_MODE = False
Config.IMPLICIT_WAIT = 10
Config.EXPLICIT_WAIT = 15
```

### Environment URLs
```python
# Update URLs for different environments
Config.get_base_url(Environment.DEV)    # Development
Config.get_base_url(Environment.TEST)   # Testing
Config.get_base_url(Environment.PROD)   # Production
```

### Test Data
```python
# Modify test credentials
credentials = Config.get_test_credentials()
```

## 🎯 Best Practices

### 1. Element Locators
```python
# Prefer CSS selectors and XPath
USERNAME = (By.CSS_SELECTOR, "input[name='username']")
PASSWORD = (By.XPATH, "//input[@type='password']")
```

### 2. Wait Strategies
```python
# Use explicit waits instead of sleep
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(locator))
```

### 3. Error Handling
```python
try:
    element.click()
except ElementNotInteractableException:
    # Fallback to JavaScript click
    driver.execute_script("arguments[0].click();", element)
```

### 4. Page Object Model
```python
class LoginPage(BasePage):
    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
```

## 🐛 Troubleshooting

### Common Issues

#### 1. ChromeDriver Version Mismatch
```bash
# Install webdriver-manager for auto-management
pip install webdriver-manager
```

#### 2. Element Not Found
- Check element locators
- Add appropriate waits
- Verify page load state

#### 3. Tests Running Slowly
- Use headless mode
- Optimize wait times
- Disable images/CSS loading

#### 4. Permission Denied (Linux)
```bash
chmod +x run_tests.py
```

## 📈 Extending the Framework

### Add New Page Objects
```python
class NewPage(EnhancedBasePage):
    # Define locators
    BUTTON = (By.ID, "submit-btn")
    
    def click_submit(self):
        return self.click_element(self.BUTTON)
```

### Add New Test Cases
```python
def test_new_functionality():
    page = NewPage(driver)
    result = page.click_submit()
    assert result is True
```

### Add Custom Utilities
```python
class CustomUtilities(EnhancedBasePage):
    def upload_file(self, file_path):
        # Custom file upload logic
        pass
    
    def handle_alert(self):
        # Custom alert handling
        pass
```

## 🔍 Advanced Features

### Data-Driven Testing
```python
import pytest

@pytest.mark.parametrize("username,password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("user3", "pass3")
])
def test_login_multiple_users(username, password):
    # Test with different user combinations
    pass
```

### Parallel Execution
```bash
# Run tests in parallel
pip install pytest-xdist
pytest -n 4 selenium_examples.py
```

### Cross-Browser Testing
```python
@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_cross_browser(browser):
    driver = setup_driver(browser)
    # Run test across different browsers
```

## 📚 Additional Resources

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [WebDriver Best Practices](https://www.selenium.dev/documentation/webdriver/)
- [Page Object Model Pattern](https://selenium-python.readthedocs.io/page-objects.html)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Happy Testing! 🎉**