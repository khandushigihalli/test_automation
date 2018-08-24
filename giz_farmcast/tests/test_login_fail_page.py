import time
from selenium.webdriver.chrome import webdriver, options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ChromeOptions, Chrome

from giz_farmcast.tests.farmcast_web.pages import driver
from giz_farmcast.tests.farmcast_web.pages.login_page import LoginPage

login_page = LoginPage(driver)

#1)test-case to test login-unsucessful
def test_login_fail():
        login_page.phone_number_element = "9108"
        login_page.password = "khan8521"
        time.sleep(2)
        driver.find_element_by_id('password').clear()
        login_page.click_go_button()
        time.sleep(2)
        assert login_page.verifyError()

#2)test-case test mobile-number field with-out mobile-number input
def test_without_mobilenumber():
        login_page.phone_number_element = ''
        driver.find_element_by_id('password').clear()
        login_page.password = 'khand8521'
        login_page.click_go_button()
        time.sleep(2)
        assert login_page.test_mobile_number_without_input()

#3)test-case to test unregistered mobile-number
def test_for_unregistered_mobile_number():
        login_page.phone_number_element = '8095304627'
        time.sleep(2)
        login_page.password = 'khand8521'
        driver.find_element_by_id('password').clear()
        login_page.click_go_button()
        time.sleep(2)
        assert login_page.test_unregistered_mobile_number()

#4)test-case to test whether mobile-number accepts more than 10 digits
def test_for_morethan_10digits_mobile_number():
        login_page.phone_number_element = '809530462712345'
        login_page.password = 'khand8521'
        driver.find_element_by_id('password').clear()
        login_page.click_go_button()
        time.sleep(2)
        assert login_page.test_morethan_10digits_mobile_number()

#5)test-case to test whether mobile-number field accepts string-value or not
def test_mobile_number_accepts_string_as_input():
        login_page.phone_number_element = 'khandushigihalli'
        login_page.password = 'khan8521'
        driver.find_element_by_id('password').clear()
        login_page.click_go_button()
        time.sleep(2)
        assert login_page.test_mobile_with_string()

#6)test-case to test password field without Password as input
def test_without_password():
        login_page.phone_number_element = '9108668521'
        login_page.password = ''
        login_page.click_go_button()
        time.sleep(2)
        assert login_page.test_passwordfield_without_input()
        time.sleep(2)

#7)test-case to test mobile-number field and password with empty-input
def test_for_empty_input():
        login_page.phone_number_element = ''
        login_page.password = ''
        login_page.click_go_button()
        time.sleep(2)
        assert login_page.test_empty_input()

#8)test-case to test with registered mobile-number and wrong password
def test_for_invalid_password():
        login_page.phone_number_element = '9108668521'
        login_page.password = '8521khan'
        login_page.click_go_button()
        time.sleep(2)
        assert login_page.test_for_invalid_password()
        cleanup()

def cleanup(self):
       self.driver.close()