from giz_farmcast.tests.farmcast_web.elements.base_page_element import BasePageElement


class LoginPageTitleSearch(BasePageElement):
    locator = '//*[@id=\"unauthenticated\"]/form/h2'

class LoginPageUserNameElement(BasePageElement):
    locator = 'phone_number'

class LoginPagePassWordElement(BasePageElement):
    locator = 'password'

class LoginPageSubmitButtonElement(BasePageElement):
    locator = 'submit'

class LoginPageError(BasePageElement):
    locator = '//*[@id=\"unauthenticated\"]/form/p'

class LoginPageMobileNumberError(BasePageElement):
    locator = '//*[@id=\"unauthenticated\"]/form/p'

class DashBoardCropsMenuElement(BasePageElement):
    locator = '//*[@id=\"mainContainer\"]/paper-menu/div/a[2]/span'

class DashBoardProductsMenuElement(BasePageElement):

    locator = '//*[@id=\"mainContainer\"]/paper-menu/div/a[3]/span'

class DashBoardGroupsMenuElement(BasePageElement):
    locator = '//*[@id=\"mainContainer\"]/paper-menu/div/a[4]/span'

class DashBoardUsersMenuElement(BasePageElement):
    locator = '//*[@id=\"mainContainer\"]/paper-menu/div/a[5]/span'

class DashBoardFarmersMenuElement(BasePageElement):
    locator = '//*[@id=\"mainContainer\"]/paper-menu/div/a[6]/span'

class DashBoardHarvestMenuElement(BasePageElement):
    locator = '//*[@id=\"mainContainer\"]/paper-menu/div/a[7]/span'

class DashBoardAgriInputsMenuElement(BasePageElement):
    locator = '//*[@id=\"mainContainer\"]/paper-menu/div/a[8]/span'

class CreateCropsButtonElement(BasePageElement):
    locator = 'btnCreate'

# class CreateCropsButtonElement1(BasePageElement):
#     locator = '//*[@id=\"btnCreate\"]'

class InputValueElement(BasePageElement):
    locator = 'name'
class CropVarietyElement(BasePageElement):
    locator = 'variety'

class ClickButton(BasePageElement):
    locator = '//*[@id=\"container\"]/new-crop/div/div/div/div[2]/div/paper-button[1]'

class DropDown(BasePageElement):
    locator = '//*[@id=\"trigger\"]/div/paper-input/paper-input-container/div[1]/iron-icon'

class Value(BasePageElement):
    locator = '//*[@id=\"contentWrapper\"]/div/paper-menu/div/paper-item[4]'

class Edit(BasePageElement):
    locator = '//*[@id=\"container\"]/table/tbody/tr[1]/td[4]/div/span/span/shibui-dropdown-menu/div/div'

class SelectEdit(BasePageElement):
    locator = '//*[@id=\"dropdown\"]/a[1]'

class LandPreparation(BasePageElement):
    locator = '//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[2]/div/div[1]'

class checkAssert(BasePageElement):
    locator = '//*[@id=\"topBlock\"]/div[1]/span'

class SoilTypeElement(BasePageElement):
    locator = 'soil'

class SeasonElement(BasePageElement):
    locator = 'season'

class PreparationLandElement(BasePageElement):
    locator = 'land_preparation'

class NurseryElement(BasePageElement):
    locator = 'nursery'

class LandPreparationSubmit(BasePageElement):
    locator = '//*[@id=\"selector\"]/mtz-wizard-step[2]/div[3]/div/paper-button[1]'

class Fertigation(BasePageElement):
    locator = '//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[3]/div/div[1]'

class InputDemand(BasePageElement):
    locator = '//*[@id=\"topBlock\"]/div[1]/span'

class DashBoardElement(BasePageElement):
    locator = '//*[@id=\"mainContainer\"]/paper-menu/div/a[1]/span'

class Top(BasePageElement):
    locator = '//*[@id=\"container\"]/home-view/bootstrap-grid/div[2]/div/div/div[1]/h4'

class Members(BasePageElement):
    locator = '//*[@id=\"topBlock\"]/div[1]/span'

class Product(BasePageElement):
    locator = '//*[@id=\"topBlock\"]/div[1]/span'

class Users(BasePageElement):
    locator = '//*[@id=\"topBlock\"]/div[1]/span'

class Harvests(BasePageElement):
    locator = '//*[@id=\"topBlock\"]/div[1]/span'

class Groups(BasePageElement):
    locator = '//*[@id=\"topBlock\"]/div[1]/span'

class Click(BasePageElement):
    locator = '//*[@id=\"container\"]/new-crop/div/div/div/div[2]/div/paper-button[1]'

class verifyHeading(BasePageElement):
    locator = '//*[@id=\"container\"]/edit-crop/div/div/div/div/div[1]/div[1]/h3'

# class verifyCropName(BasePageElement):
#     locator = 'mainContainer'

class Cropheading(BasePageElement):
    locator = 'mainContainer'

class Cnames(BasePageElement):
    locator = '//*[@id=\"title\"]'


class SelectLanguage(BasePageElement):
     locator = '//*[@id=\"input\"]'

class CropDuration(BasePageElement):
    locator = 'duration'

class CropFrequency(BasePageElement):
    locator = 'frequency'

class CropAge(BasePageElement):
    locator = 'input'

class CropSelectLang(BasePageElement):
    locator = '//*[@id=\"language\"]/paper-input-container/div[2]'

class Fertilizer(BasePageElement):
    locator = 'fertilizer'

class TemplateElement(BasePageElement):
    locator = 'template'


class TotalFertilizer(BasePageElement):
    locator = 'totalFertilizer'


class CropEditSubmitButtonElement(BasePageElement):
    locator = '//*[@id=\"container\"]/crop-fertilizer-schedule/div[2]/div[3]/div/paper-button[1]'

class CropInfoUpdate(BasePageElement):
    locator = 'toast'


class IrrigationElement(BasePageElement):
    locator = 'input'


class ManureElement(BasePageElement):
    locator = 'textarea'


class SubmitElement(BasePageElement):
    locator = '//*[@id=\"selector\"]/mtz-wizard-step[4]/div/div/paper-button[1]'

class Back_ButtonElement(BasePageElement):
    locator = '//*[@id=\"icon\"]'

class Page_NextElement(BasePageElement):
    locator = '//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[5]/div/div[1]'

class Next_page(BasePageElement):
    locator = '//*[@id=\"container\"]/edit-crop/div/div/div/div/div[2]/mtz-wizard-stepper/div[4]/div/div[1]'


class Info1_page(BasePageElement):
    locator = '//*[@id=\"toast\"]'

class HarvestGrade(BasePageElement):
    locator = 'grading'

class HarvestSubmit(BasePageElement):
    locator = '//*[@id=\"selector\"]/mtz-wizard-step[5]/div/div/paper-button[1]'

class ToastMessage(BasePageElement):
    locator = 'toast'


