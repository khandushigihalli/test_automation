from giz_farmcast.tests.farmcast_web.elements.element import DashBoardAgriInputsMenuElement
from giz_farmcast.tests.farmcast_web.locators.locators import DashBoardLocators
from giz_farmcast.tests.farmcast_web.pages.base_page import BasePage


class AgriInputs(BasePage):
    agriinputs_menu_element = DashBoardAgriInputsMenuElement()

    def test_dashboard_agriinput_click(self):
        agriinputs_menu_element = self.driver.find_element(*DashBoardLocators.AGRI_INPUTS_MENU)
        agriinputs_menu_element.click()
        # assert agriinputs_menu_element

    def CheckForInputDemand(self):
        element3 = self.driver.find_element(*DashBoardLocators.INPUT_DEMAND)
        return element3.text == 'Input Demand'