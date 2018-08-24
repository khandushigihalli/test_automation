from giz_farmcast.tests.farmcast_web.elements.element import DashBoardFarmersMenuElement
from giz_farmcast.tests.farmcast_web.locators.locators import DashBoardLocators
from giz_farmcast.tests.farmcast_web.pages.base_page import BasePage


class FarmersPage(BasePage):
    farmers_menu_element = DashBoardFarmersMenuElement()

    def test_dashboard_farmersmenu_click(self):
        farmers_menu_element = self.driver.find_element(*DashBoardLocators.FARMERS_MENU)
        farmers_menu_element.click()

    def test_members_farmersmenu(self):
        m =self.driver.find_element(*DashBoardLocators.MEMBERS)
        return m.text == 'Members'