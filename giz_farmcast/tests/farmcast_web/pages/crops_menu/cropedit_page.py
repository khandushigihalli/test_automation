import time

from tests.farmcast_web.elements.element import Edit
from tests.farmcast_web.locators.locators import DashBoardLocators
from tests.farmcast_web.pages.base_page import BasePage


class CropEdit(BasePage):

    crop_edit = Edit()

    def drop_down_Value_select(self):
        drop_down = self.driver.find_element(*DashBoardLocators.DROP_DOWN)
        drop_down.click()


    def vlaue(self):
        value = self.driver.find_element(*DashBoardLocators.VALUE)
        value.click()

    def createdcroppresent(self):
        cropcheck = self.driver.find_element(*DashBoardLocators.CROPD)
        return cropcheck.text == 'verify12'


    def clickEdit(self):
        edit = self.driver.find_element(*DashBoardLocators.EDIT)
        edit.click()


    def selectEdit(self):
        selectedit = self.driver.find_element(*DashBoardLocators.S_EDIT)
        selectedit.click()
        time.sleep(2)



