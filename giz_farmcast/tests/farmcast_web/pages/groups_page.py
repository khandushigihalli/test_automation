from giz_farmcast.tests.farmcast_web.elements.element import DashBoardGroupsMenuElement
from giz_farmcast.tests.farmcast_web.locators.locators import DashBoardLocators
from giz_farmcast.tests.farmcast_web.pages.base_page import BasePage


class GroupsPage(BasePage):
    groups_menu_element = DashBoardGroupsMenuElement()

    def test_dashboard_groups_click(self):
        groups_menu_element = self.driver.find_element(*DashBoardLocators.GROUPS_MENU )
        groups_menu_element.click()


    def test_Groups(self):
            g = self.driver.find_element(*DashBoardLocators.GROUPS)
            return g.text == 'Groups'


