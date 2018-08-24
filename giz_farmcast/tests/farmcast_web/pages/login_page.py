import time

from giz_farmcast.tests.farmcast_web.elements.element import LoginPageUserNameElement, LoginPagePassWordElement
from giz_farmcast.tests.farmcast_web.locators.locators import LoginLocators
from giz_farmcast.tests.farmcast_web.pages.base_page import BasePage


class LoginPage(BasePage):
    phone_number_element = LoginPageUserNameElement()
    password = LoginPagePassWordElement()

    def test_login_successful_for_registered_user(self):
        phone_number_element = self.driver.find_element(*LoginLocators.USER_NAME)
        time.sleep(2)

    def test_login_successful_for_OTP(self):
        password = self.driver.find_element(*LoginLocators.PASSWORD)
        time.sleep(2)


    def click_go_button(self):
        element = self.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        element.click()

    def is_title_matches(self):
        title = self.driver.find_element(*LoginLocators.TITLE)
        return title.text == 'Login to Easykrishi'

    def verifyError(self):
        error = self.driver.find_element(*LoginLocators.CHECK)
        return error.text == 'Error: User not registered'

    def test_mobile_number_without_input(self):
        mob = self.driver.find_element(*LoginLocators.DATA)
        return mob.text == 'Error:  Invalid data'

    def test_passwordfield_without_input(self):
        pas = self.driver.find_element(*LoginLocators.DATA)
        return pas.text == 'Error: Invalid data'

    def test_unregistered_mobile_number(self):
        pas1 = self.driver.find_element(*LoginLocators.CHECK)
        return pas1.text == 'Error: User not registered'

    def test_morethan_10digits_mobile_number(self):
        pas2 = self.driver.find_element(*LoginLocators.CHECK)
        return pas2.text == 'Error: User not registered'

    def test_mobile_with_string(self):
        str = self.driver.find_element(*LoginLocators.CHECK)
        return str.text == 'Error: Ivalid data'

    def test_empty_input(self):
        empty = self.driver.find_element(*LoginLocators.DATA)
        return empty.text == 'Error: Ivalid data'

    def test_for_invalid_password(self):
        invaliddata = self.driver.find_element(*LoginLocators.DATA)
        return invaliddata.text == 'Error: User not registered'

    def test_for_upper_case_password(self):
        upper = self.driver.find_element(*LoginLocators.DATA)
        return upper.text == ''
