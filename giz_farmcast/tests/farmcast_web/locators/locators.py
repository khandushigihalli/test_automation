from selenium.webdriver.common.by import By

class Locators(object):
    TITLE = (By.XPATH,'//*[@id=\"unauthenticated\"]/form/h2')


class LoginLocators(object):
    # TITLE = (By.XPATH,'//*[@id=\"unauthenticated\"]/form/h2')
    USER_NAME = (By.ID,'phone_number')
    PASSWORD = (By.ID,'password')
    LOGIN_BUTTON = (By.ID, 'submit')
    CHECK = (By.XPATH, '//*[@id=\"unauthenticated\"]/form/p')
    DATA = (By.XPATH,'//*[@id=\"unauthenticated\"]/form/p')


class DashBoardLocators(object):
    CROPS_MENU = (By.XPATH,'//*[@id=\"mainContainer\"]/paper-menu/div/a[2]/span')
    PRODUCT_MENU = (By.XPATH,'//*[@id=\"mainContainer\"]/paper-menu/div/a[3]/span')
    GROUPS_MENU = (By.XPATH,'//*[@id=\"mainContainer\"]/paper-menu/div/a[4]/span')
    USERS_MENU = (By.XPATH,'//*[@id=\"mainContainer\"]/paper-menu/div/a[5]/span')
    FARMERS_MENU = (By.XPATH,'//*[@id=\"mainContainer\"]/paper-menu/div/a[6]/span')
    HARVERST_MENU = (By.XPATH, '//*[@id=\"mainContainer\"]/paper-menu/div/a[7]/span')
    AGRI_INPUTS_MENU = (By.XPATH, '//*[@id=\"mainContainer\"]/paper-menu/div/a[8]/span')
    CREATEBUTTON = (By.ID,'btnCreate')
    CROPNAME = (By.ID,'name')
    VARIETY = (By.ID,'variety')
    CLICK_BUTTON = (By.XPATH, '//*[@id=\"container\"]/new-crop/div/div/div/div[2]/div/paper-button[1]')
    DROP_DOWN = (By.XPATH,'//*[@id=\"trigger\"]/div/paper-input/paper-input-container/div[1]/iron-icon')
    VALUE = (By.XPATH,'//*[@id=\"contentWrapper\"]/div/paper-menu/div/paper-item[4]')
    EDIT = (By.XPATH,'//*[@id=\"container\"]/table/tbody/tr[1]/td[4]/div/span/span/shibui-dropdown-menu/div/div')
    S_EDIT = (By.XPATH,'//*[@id=\"dropdown\"]/a[1]')
    LAND_P = (By.XPATH, '//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[2]/div/div[1]')
    LAND_P1 = (By.XPATH,'//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[3]/div')
    VERIFY = (By.XPATH,'//*[@id=\"topBlock\"]/div[1]/span')
    SOILTYPE = (By.ID,'soil')
    SEASON = (By.ID, 'season')
    PREPATION = (By.ID, 'land_preparation')
    NURSERY = (By.ID, 'nursery')
    SUB = (By.XPATH,'//*[@id=\"selector\"]/mtz-wizard-step[2]/div[3]/div/paper-button[1]')
    FERTIGATION = (By.XPATH,'//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[3]/div/div[1]')
    INPUT_DEMAND = (By.XPATH,'//*[@id=\"topBlock\"]/div[1]/span')
    DASH_BOARD = (By.XPATH, '//*[@id=\"mainContainer\"]/paper-menu/div/a[1]/span')
    TOP = (By.XPATH,'//*[@id=\"container\"]/home-view/bootstrap-grid/div[2]/div/div/div[1]/h4')
    MEMBERS = (By.XPATH, '//*[@id=\"topBlock\"]/div[1]/span')
    PRODUCT = (By.XPATH,'//*[@id=\"topBlock\"]/div[1]/span')
    USERS = (By.XPATH, '//*[@id=\"topBlock\"]/div[1]/span')
    HARVEST = (By.XPATH,'//*[@id=\"topBlock\"]/div[1]/span')
    GROUPS = (By.XPATH,'//*[@id=\"topBlock\"]/div[1]/span')
    CLICK = (By.XPATH,'//*[@id=\"container\"]/new-crop/div/div/div/div[2]/div/paper-button[1]')
    ST = (By.XPATH,'//*[@id=\"container\"]/edit-crop/div/div/div/div/div[1]/div[1]/h3')
    CROPD = (By.ID,'mainContainer')
    HEADING = (By.XPATH,'mainContainer')
    CNAME = (By.XPATH,'//*[@id=\"title\"]')
    LANGUAGE_SELECT = (By.XPATH,'//*[@id=\"input\"]')
    DURATION = (By.ID,'duration')
    FREQUENCY = (By.ID,'frequency')
    CROP_AGE = (By.ID,'input')
    SELECT_L = (By.XPATH,'//*[@id=\"language\"]/paper-input-container/div[2]')
    FERTILIZER = (By.ID,'fertilizer')
    TEMPLATE = (By.ID,'template')
    TOTAL_FERTILIZER = (By.ID,'totalFertilizer')
    SUBMIT = (By.XPATH,'//*[@id=\"container\"]/crop-fertilizer-schedule/div[2]/div[3]/div/paper-button[1]')
    INFO = (By.ID,'toast')
    IRRIGATION = (By.ID,'input')
    MANURE = (By.ID,'textarea')
    IRRI_SUBMIT =  (By.XPATH,'//*[@id=\"selector\"]/mtz-wizard-step[4]/div/div/paper-button[1]')
    BACK_BUTTON = (By.XPATH,'//*[@id=\"icon\"]')
    NEXT_PAGE = (By.XPATH,'//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[4]/div/div[1]')
    INFO1 = (By.XPATH,'//*[@id=\"toast\"]')
    PAGE_NEXT = (By.XPATH,'//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[5]/div/div[1]')
    GRADING = (By.ID,'grading')
    CURING = (By.ID,'curing')
    HARVEST_SUBMIT = (By.XPATH,'//*[@id=\"selector\"]/mtz-wizard-step[5]/div/div/paper-button[1]')
    TOAST =(By.ID,'toast')
