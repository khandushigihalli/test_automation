from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from tests.farmcast_web.elements.element import CreateCropsButtonElement, InputValueElement, CropDuration, \
    CropFrequency, CropAge, CropSelectLang, Fertilizer, TemplateElement, TotalFertilizer
from tests.farmcast_web.locators.locators import DashBoardLocators
from tests.farmcast_web.pages.base_page import BasePage


class FertigationElement(BasePage):
    create_page = CreateCropsButtonElement()
    input = InputValueElement()
    duration = CropDuration()
    frequency = CropFrequency()
    cropage = CropAge()
    # selectLang = CropSelectLang()
    fertilizer =Fertilizer()
    template =  TemplateElement()
    totalFertilizer = TotalFertilizer()


    def FertigationCrop(self):
        fertigation  = self.driver.find_element(*DashBoardLocators.LAND_P1)
        fertigation.click()

    def test_create_crops_button1(self):
        crops_menu1 = self.driver.find_element(*DashBoardLocators.CREATEBUTTON)
        crops_menu1.click()

    def test_input_value(self):
        input = self.driver.find_element(*DashBoardLocators.CROPNAME)


    def test_duration(self):
        duration = self.driver.find_element(*DashBoardLocators.DURATION)


    def test_cropage(self):
        frequency= self.driver.find_element(*DashBoardLocators.FREQUENCY )

    def test_duration(self):
        cropage = self.driver.find_element(*DashBoardLocators.CROP_AGE)

    def test_select_language(self):
        selectLang = self.driver.find_element(*DashBoardLocators.CROP_AGE)
        # selectLang.send_keys(Keys.RETURN)
        selectLang.click()

    def test_for_fertilizer(self):
        fertilizer = self.driver.find_element(*DashBoardLocators.FERTILIZER)

    def test_for_Template(self):
        template = self.driver.find_element(*DashBoardLocators.TEMPLATE)

    def test_total_fertilizer(self):
        totalFertilizer = self.driver.find_element(*DashBoardLocators.TOTAL_FERTILIZER)

    def submit_button(self):
        submit = self.driver.find_element(*DashBoardLocators.SUBMIT)
        submit.click()

    def verify_backButton_click(self):
        backbutton = self.driver.find_element(*DashBoardLocators.BACK_BUTTON)
        backbutton.click()

    def test_next_page(self):
        next_screen = self.driver.find_element(*DashBoardLocators.NEXT_PAGE)
        next_screen.click()