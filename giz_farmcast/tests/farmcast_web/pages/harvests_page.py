from giz_farmcast.tests.farmcast_web.elements.element import DashBoardHarvestMenuElement
from giz_farmcast.tests.farmcast_web.locators.locators import DashBoardLocators
from giz_farmcast.tests.farmcast_web.pages.base_page import BasePage


class HarvestsPage(BasePage):
    harvests_menu_element = DashBoardHarvestMenuElement()

    def test_dashboard_harvests_click(self):
        harvests_menu_element = self.driver.find_element(*DashBoardLocators.HARVERST_MENU)
        harvests_menu_element.click()

    def test_Harvests(self):
        u = self.driver.find_element(*DashBoardLocators.HARVEST)
        return u.text == 'Expected Harvest'
