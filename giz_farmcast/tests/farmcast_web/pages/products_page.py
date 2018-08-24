from giz_farmcast.tests.farmcast_web.elements.element import DashBoardProductsMenuElement
from giz_farmcast.tests.farmcast_web.locators.locators import DashBoardLocators
from giz_farmcast.tests.farmcast_web.pages.base_page import BasePage


class ProductsPage(BasePage):
    products_menu_element = DashBoardProductsMenuElement()

    def test_dashboard_products_click(self):
        products_menu_element = self.driver.find_element(*DashBoardLocators.PRODUCT_MENU)
        products_menu_element.click()


    def test_Products_Visible(self):
         p = self.driver.find_element(*DashBoardLocators.PRODUCT)
         return p.text == 'Products'