import time

from marketing_app.testcases.farmcast_buyer.elements.element import LoginPageUserPhoneNumberElement
from marketing_app.testcases.farmcast_buyer.locators.locator import LoginLocators
from marketing_app.testcases.farmcast_buyer.pages.base_page import BasePage


class BuyerLoginPage(BasePage):
    phone_number_element = LoginPageUserPhoneNumberElement()


    def test_login_successful_for_registered_user(self):
        phone_number_element = self.driver.find_element(*LoginLocators. MOBILE_NUMBER)


    def click_go_button(self):
        element = self.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        element.click()