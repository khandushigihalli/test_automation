import time

from tests.farmcast_web.elements.element import DashBoardCropsMenuElement
from tests.farmcast_web.locators.locators import DashBoardLocators
from tests.farmcast_web.pages.base_page import BasePage


class CropsPage(BasePage):
    crops_menu_element = DashBoardCropsMenuElement()

    def test_dashboard_crops_click(self):
        crops_menu_element = self.driver.find_element(*DashBoardLocators.CROPS_MENU)
        crops_menu_element.click()
        time.sleep(2)

    def CheckForCrops_View(self):
        element = self.driver.find_element(*DashBoardLocators.VERIFY)
        return element.text == 'Crops'

