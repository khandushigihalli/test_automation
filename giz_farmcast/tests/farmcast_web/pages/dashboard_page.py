import time
from _ast import Assert
from tokenize import String

from giz_farmcast.tests.farmcast_web.elements.element import DashBoardElement
from giz_farmcast.tests.farmcast_web.locators.locators import DashBoardLocators
from giz_farmcast.tests.farmcast_web.pages.base_page import BasePage


class DashboardPage(BasePage):
    dashboard_element = DashBoardElement()


    def test_dashboard(self):
        time.sleep(10)
        self.driver.refresh()
        time.sleep(2)
        dashboard_element = self.driver.find_element(*DashBoardLocators.DASH_BOARD)
        dashboard_element.click()
        time.sleep(2)


    def test_successfulIntoDashBoard(self):
        ele = self.driver.find_element(*DashBoardLocators.TOP)
        return ele.text == 'Top produce'

