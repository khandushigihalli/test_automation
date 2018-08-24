import unittest

from selenium import webdriver


class BaseTestCase():
    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options= options, options= options)
        self.driver.get("http://35.154.213.24")

    def tearDown(self):
        self.driver.close()
