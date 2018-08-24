from tests.farmcast_web.elements.element import IrrigationElement, ManureElement
from tests.farmcast_web.locators.locators import DashBoardLocators
from tests.farmcast_web.pages.base_page import BasePage


class IrrigationElement(BasePage):
    irrigation_element = IrrigationElement()
    manure_element = ManureElement()


    def test_irrigation_input_data(self):
        irrigation_element = self.driver.find_element(*DashBoardLocators.IRRIGATION)

    def test_irrigation_input_data(self):
        irrigation_element = self.driver.find_element(*DashBoardLocators.MANURE)


    def test_irrigation_Submit(self):
        irrigation_submit = self.driver.find_element(*DashBoardLocators.IRRI_SUBMIT)
        irrigation_submit.click()


    def test_toast_message_display(self):
        info1 = self.driver.find_element(*DashBoardLocators.INFO1)
        return info1.text == 'Crop updated successfully Ok'


    def test_next_page_display(self):
        page_next = self.driver.find_element(*DashBoardLocators.PAGE_NEXT)
        page_next.click()

