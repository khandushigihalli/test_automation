from tests.farmcast_web.elements.element import HarvestGrade
from tests.farmcast_web.locators.locators import DashBoardLocators
from tests.farmcast_web.pages.base_page import BasePage

class PostHarvestElement(BasePage):
    grading_element = HarvestGrade()

    def test_for_harvest(self):
        grading_element =self.driver.find_element(*DashBoardLocators.GRADING)

    def test_for_submitButton(self):
        submit = self.driver.find_element(*DashBoardLocators.HARVEST_SUBMIT)
        submit.click()

    def test_for_harvest_complete_toast_message(self):
        harvest_complete = self.driver.find_element(*DashBoardLocators.TOAST)
        return harvest_complete.text == 'Crop updated successfully Ok'