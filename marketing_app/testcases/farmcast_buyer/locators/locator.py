from selenium.webdriver.common.by import By


class LoginLocators(object):
    MOBILE_NUMBER = (By.ID,'login_phonenumber')
    LOGIN_BUTTON = (By.ID, 'login_button')