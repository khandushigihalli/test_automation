from giz_farmcast.tests.farmcast_web.elements.element import DashBoardUsersMenuElement
from giz_farmcast.tests.farmcast_web.locators.locators import DashBoardLocators
from giz_farmcast.tests.farmcast_web.pages.base_page import BasePage


class UsersPage(BasePage):
    users_menu_element = DashBoardUsersMenuElement()

    def test_dashboard_usersmenu_click(self):
        users_menu_element = self.driver.find_element(*DashBoardLocators.USERS_MENU)
        users_menu_element.click()

    def test_Users(self):
        u = self.driver.find_element(*DashBoardLocators.USERS)
        return  u.text == 'Users'