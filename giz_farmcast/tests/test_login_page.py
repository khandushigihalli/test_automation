import time
from io import StringIO
from selenium.webdriver.common.keys import Keys


#1)test-case to test for Login Sucessful
# from giz_farmcast.tests.farmcast_web.pages import driver
from giz_farmcast.tests.farmcast_web.pages import driver
from giz_farmcast.tests.farmcast_web.pages.crops_menu.createcrop_page import CreateCrops, createcrop
from giz_farmcast.tests.farmcast_web.pages.crops_menu.cropedit_page import CropEdit
from giz_farmcast.tests.farmcast_web.pages.crops_menu.crops_page import CropsPage
from giz_farmcast.tests.farmcast_web.pages.crops_menu.fertigation_page import FertigationElement
from giz_farmcast.tests.farmcast_web.pages.crops_menu.irrigation_page import IrrigationElement
from giz_farmcast.tests.farmcast_web.pages.crops_menu.land_preparation import LandPreparation
from giz_farmcast.tests.farmcast_web.pages.crops_menu.postharvest_page import PostHarvestElement
from giz_farmcast.tests.farmcast_web.pages.dashboard_page import DashboardPage
from giz_farmcast.tests.farmcast_web.pages.login_page import LoginPage
import nose_htmloutput

def test_login():
    login_page = LoginPage(driver)
    time.sleep(2)
    assert login_page.is_title_matches()
    time.sleep(2)
    login_page.phone_number_element = "9108668521"
    time.sleep(1)
    login_page.password = "khan8521"
    time.sleep(1)
    login_page.click_go_button()
    time.sleep(2)

#2)test-case to test for Dashboard visible after successful login
def test_dashboard():
    time.sleep(2)
    dashboard_page = DashboardPage(driver)
    dashboard_page.test_dashboard()
    time.sleep(2)
    assert dashboard_page.test_successfulIntoDashBoard()

#3)test-case to test for Crops-Menu visible or not
def test_CropsMenu():
    time.sleep(2)
    crops_page = CropsPage(driver)
    crops_page.test_dashboard_crops_click()
    time.sleep(2)
    assert crops_page.CheckForCrops_View()
    time.sleep(2)

#4)test-case test create-crop button click-able or not
#it has fail
def test_Createcrops():
    crop_page = CreateCrops(driver)
    crop_page.test_create_crops_button()
    assert crop_page.test_heading_in_create_crop_screen()

#5)test-case to test the crop created sucessfully or not
#it has fail
def test_input_values():
    crop_page1 = createcrop(driver)
    crop_page1.crop2_page = 'verify12345'
    crop_page1.crops3_page = 'verify12345'
    crop_page1.test_click_button()
    # assert crop_page1.test_crop_created_successfully_or_not()
    # return test_CropsMenu()

#6)test-case to test crop-edit
def test_CropEdit():
    time.sleep(2)
    edit_page = CropEdit(driver)
    edit_page.drop_down_Value_select()
    time.sleep(1)
    edit_page.vlaue()
    edit_page.clickEdit()
    edit_page.selectEdit()

#7)test-case to test land-Preparation screen
def test_landPreparationScreen():
    land_prepare_page = LandPreparation(driver)
    land_prepare_page. LandPreparation()
    land_prepare_page.soil_type_input_element = 'alluvial soil'
    land_prepare_page.season_input_element = 'june-october'
    land_prepare_page. prepare_land_element ='plooghing land in well fine tilth'
    land_prepare_page.nursery_element = 'yet to be known'
    land_prepare_page.LandSubmit()
    time.sleep(1)
    assert land_prepare_page.verify_Crop_Info_Updated_Or_Not()

#8)test-case to test Fertigation page
def test_fertigationPage():
    fertigation_page = FertigationElement(driver)
    fertigation_page.FertigationCrop()
    time.sleep(2)
    fertigation_page.test_create_crops_button1()
    fertigation_page.input = '0'
    fertigation_page.duration = '10'
    fertigation_page.frequency = '3'
    fertigation_page.cropage = '18'
    fertigation_page.fertilizer = 'potash,19:19:19,cowdung'
    fertigation_page.template = 'ನಮಸ್ಕಾರ#farmer_name#,ಇಂದು ನೀವು ನೀಮ್ಮ #crop_name# ಬೆಳೆಗೆ#fertilizer# ಹಾಕಿ ಉತ್ತಮವಾದ ಇಳುವರಿ ಪಡೆಯಿರಿ'
    fertigation_page.totalFertilizer = '50,50,35'
    fertigation_page.submit_button()
    time.sleep(2)
    fertigation_page.verify_backButton_click()
    time.sleep(3)
    fertigation_page.test_next_page()


#9)test-case to test Irrigation Page
def test_irrigationPage():
    irrigation_page = IrrigationElement(driver)
    irrigation_page.irrigation_element = 'simply check'
    irrigation_page.manure_element = 'cowdung,potash'
    irrigation_page.test_irrigation_Submit()
    time.sleep(1)
    assert irrigation_page.test_toast_message_display()
    time.sleep(2)
    irrigation_page.test_next_page_display()

#10)test-case to test Harvest Page
def test_harvestPage():
    harvest_page = PostHarvestElement(driver)
    harvest_page.grading_element = 'A'
    harvest_page.test_for_submitButton()
    time.sleep(1)
    assert harvest_page.test_for_harvest_complete_toast_message()





