import time

from marketing_app.testcases.farmcast_buyer.pages import driver
from marketing_app.testcases.farmcast_buyer.pages.buyer_login_page import BuyerLoginPage


def test_login():
    BuyerLoginPage1 = BuyerLoginPage(driver)
    BuyerLoginPage1.phone_number_element = "7975132078"
    BuyerLoginPage1.click_go_button()