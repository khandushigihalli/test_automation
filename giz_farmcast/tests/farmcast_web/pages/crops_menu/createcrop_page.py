import time

from tests.farmcast_web.elements.element import CreateCropsButtonElement, InputValueElement, CropVarietyElement
from tests.farmcast_web.locators.locators import DashBoardLocators

from tests.farmcast_web.pages.base_page import BasePage


class CreateCrops(BasePage):
    create_page = CreateCropsButtonElement()

    def test_create_crops_button(self):
        crops_menu_element1 = self.driver.find_element(*DashBoardLocators.CREATEBUTTON)
        crops_menu_element1.click()

    def test_heading_in_create_crop_screen(self):
        heading = self.driver.find_element(*DashBoardLocators.HEADING)
        return heading.text == 'Create Crop'

class createcrop(BasePage):
    crop2_page = InputValueElement()
    crops3_page = CropVarietyElement()

    def test_input_values(self):
        crop2_page = self.driver.find_element(*DashBoardLocators.CROPNAME)


    def test_input_variety_values(self):
        crops3_page = self.driver.find_element(*DashBoardLocators.VARIETY)


    def test_click_button(self):
        crops4 = self.driver.find_element(*DashBoardLocators.CLICK_BUTTON)
        crops4.click()
        time.sleep(2)

    def test_crop_created_successfully_or_not(self):
        successful = self.driver.find_element(*DashBoardLocators.INFO)
        return successful.text == 'Crop Created Successfully'



