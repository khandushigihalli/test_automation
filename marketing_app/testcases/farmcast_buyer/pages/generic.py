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
browser.get('http://35.154.213.24')
#

def expand_shadow_element(element):
  shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
  return  shadow_root
  # root1 = browser.find_element_by_tag_name('register-login')
  # shadow_root1 = expand_shadow_element(root1)

# def find_shadow_element(root,level):
#   shadow_root = root
#
#   for i in 3:
#     print(i)
#     #shadow_root = expand_shadow_element(shadow_root)
#
#   return shadow_root
#
#
# root1 = browser.find_element_by_tag_name('register-login')
#
# find_shadow_element(root1,1)
#
#
#
#



root1 = browser.find_element_by_tag_name('register-login')

shadow_root = expand_shadow_element(root1)
loginphonenumber = shadow_root.find_element_by_id('login_phonenumber')
loginphonenumber.send_keys('7975132078')

loginbutton = shadow_root.find_element_by_id('login_button')
loginbutton.click()
time.sleep(5)


def find_shadow_element(root,level):

  shadow_root = root
  for i in range(0,level):
    print(i)
    shadow_root = expand_shadow_element(shadow_root)

  return shadow_root

home_view_root = browser.find_element_by_tag_name('home-view')

shadow_dom = find_shadow_element(home_view_root,1)

dashboard_root = shadow_dom.find_element_by_class_name('bash-board')

iron_input = find_shadow_element(dashboard_root,1)

print(iron_input)

