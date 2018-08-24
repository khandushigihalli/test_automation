from tests.farmcast_web.elements.element import SoilTypeElement, SeasonElement, \
    PreparationLandElement, NurseryElement
from tests.farmcast_web.locators.locators import DashBoardLocators
from tests.farmcast_web.pages.base_page import BasePage


class LandPreparation(BasePage):
    soil_type_input_element = SoilTypeElement()
    season_input_element = SeasonElement()
    prepare_land_element = PreparationLandElement()
    nursery_element = NurseryElement()

    def LandPreparation(self):
        landp = self.driver.find_element(*DashBoardLocators.LAND_P)
        landp.click()


    def SoilType(self):
        soil_type_input_element = self.driver.find_element(*DashBoardLocators.SOILTYPE)

    def Season(self):
        season_input_element = self.driver.find_element(*DashBoardLocators.SEASON)

    def PreparationLand(self):
        prepare_land_element = self.driver.find_element(*DashBoardLocators.PREPATION)

    def Nursery(self):
        nursery_element = self.driver.find_element(*DashBoardLocators.NURSERY)

    def LandSubmit(self):
        sub = self.driver.find_element(*DashBoardLocators.SUB)
        sub.click()

    def verify_Crop_Info_Updated_Or_Not(self):
        info = self.driver.find_element(*DashBoardLocators.INFO)
        return info.text == 'Crop updated successfully Ok'

