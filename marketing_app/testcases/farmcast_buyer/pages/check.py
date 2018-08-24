import datetime
import io
import time

import selenium
import nose_htmloutput
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.refresh()
browser.get('http://facebook.com')
time.sleep(5)
browser.find_element_by_id('email').send_keys('khandu.shigihalli@gmail.com')
browser.find_element_by_id('pass').send_keys('7259632839')
ele =  browser.find_element_by_id('u_0_2')
ele.click()

time.sleep(10)
elem =browser.find_element_by_class_name("_1vp5")
elem.click()
time.sleep(10)
browser.quit()