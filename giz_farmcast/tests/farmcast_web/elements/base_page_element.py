from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""


    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_id(self.locator))
        # driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        driver.find_element_by_id(self.locator).send_keys(value)


    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 50).until(
            lambda driver: driver.find_element_by_id(self.locator))
        element = driver.find_element_by_id(self.locator)
        return element.get_attribute("value")
        # element1 = driver.find_element_by_id(self.locator)
        # return  element.get_attribute("value")
