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
browser.get('http://35.154.213.24')
assert "Marketing App" in browser.title



def expand_shadow_element(element):
  shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root




try:
    #this is for login view
  root1 = browser.find_element_by_tag_name('register-login')
  shadow_root1 = expand_shadow_element(root1)
  print(shadow_root1)


  loginphonenumber = shadow_root1.find_element_by_id('login_phonenumber')
  loginphonenumber.send_keys('7975132078')


  loginbutton = shadow_root1.find_element_by_id('login_button')
  loginbutton.click()
  time.sleep(5)

#this for searching the crop in search-bar

  root2 = browser.find_element_by_tag_name('home-view')
  shadow_root2 = expand_shadow_element(root2)

  root3=shadow_root2.find_element_by_class_name('bash-board')
  shadow_root3 = expand_shadow_element(root3)
  time.sleep(5)

  root4 = shadow_root3.find_element_by_id('search_panel')
  shadow_root4 = expand_shadow_element(root4)


  root5 = shadow_root4.find_element_by_id('paperSearchBar')
  shadow_root5 = expand_shadow_element(root5)
  root5.send_keys('carrot')
  browser.maximize_window()
  time.sleep(10)

# hdjhjdshieiwe

    # YIuieuiewruerwiuhdjdskierurroieuuiprurirwpuwuwiw


  root6 = shadow_root3.find_element_by_id('buy_crop')
  root6.click()


#viewing the app-header view

  root7 = browser.find_element_by_tag_name('paper-icon-button')
  shadow_root7 = expand_shadow_element(root7)
  browser.find_element_by_id('cart').click()
  time.sleep(3)

#confirming the cart(shopping-cart)

  root8 = browser.find_element_by_tag_name('shopping-cart')
  shadow_root8 = expand_shadow_element(root8)


  root9 = shadow_root8.find_element_by_id('confirm_cart')
  root9.click()
  time.sleep(3)



#transportation confirmation window

  root10 = shadow_root8.find_element_by_id('transportation_dialog')
  shadow_root10 =expand_shadow_element(root10)

  root11 = shadow_root8.find_element_by_id('scroll')
  shadow_root11 = expand_shadow_element(root11)

  root13 = shadow_root8.find_element_by_id('requested_quantity')
  root13.send_keys('8')
  time.sleep(3)

  root14 = shadow_root8.find_element_by_id('requested_date')
  currentdate = datetime.datetime.today()
  root14.send_keys(datetime(currentdate, '%m-%d-%Y'))
  time.sleep(5)
  root12 = shadow_root8.find_element_by_id('check_out')
  root12.click()
  time.sleep(3)

# clicking on myorders and accessing the elements
  myorders = browser.find_element_by_xpath("//*[@id=\"drawer\"]/div/iron-selector/a[2]/span")
  myorders.click()
  time.sleep(10)


  root14 = browser.find_element_by_tag_name('my-orders')
  shadow_root14 = expand_shadow_element(root14)


  root15 = shadow_root14.find_element_by_id('selecttab')
  shadow_root15 = expand_shadow_element(root15)
  # root15.click()

  root16 = browser.find_element_by_id('request_tab')









except Exception as e:
    print (e)
    browser.quit()



browser.quit()




























# root8 = browser.find_element_by_tag_name('dash-board')
# shadow_root8 = expand_shadow_element(root8)
# print(root8)


# button = shadow_root7.find_element_by_id('search_panel')
#
#
# home = browser.find_element_by_xpath("//*[@id=\"drawer\"]/div/iron-selector/a[1]/span")
# home.click()
# time.sleep(3)
#
#
# myorders = browser.find_element_by_xpath("//*[@id=\"drawer\"]/div/iron-selector/a[2]/span")
# myorders.click()
#
# time.sleep(5)


# inner_html = browser.find_element_by_id("//*[@id=\"container\"]/my-orders//div/paper-tabs/paper-tab[1]").get_attribute("innerHTML")

#
# browser.quit()








# search = shadow_root4.find_element_by_class_name('search')
# shadow_root4 = expand_shadow_element(search)
# print(search)


# outer = expand_shadow_element(browser.find_element_by_class_name("search"))
# inner = outer.find_element_by_id("search_panel")
# inner.send_keys('sowing')




# root4 = shadow_root3.find_element_by_id('paperSearchBar')
# shadow_root4 = expand_shadow_element(root4)

# root4 = browser.find_element_by_tag_name('paper-search-panel')
# shadow_root4 = expand_shadow_element(root4)
# print(root4)

# search = shadow_root3.find_element_by_xpath('//*[@id=\"input\"]//div[2]')






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
#
# browser = webdriver.Chrome()
# browser.get("http://35.154.213.24")
# browser.find_element_by_id('phone_number').send_keys("9108668521")
# browser.find_element_by_id('password').send_keys("khan8521")
# browser.find_element_by_id('submit').click()
# time.sleep(2)
# browser.find_element_by_xpath("//*[@id=\"mainContainer\"]/paper-menu/div/a[2]/span").click()
# time.sleep(3)
# elem=browser.find_element_by_id('datatableCard')
# time.sleep(10)
# # elem.select_by_visible_text('Tomato')
# # print("sucessful")
# # time.sleep(12)
# browser.quit()



#test-case to test for Product-Menu visible or not
# def test_ProductsMenu():
#     time.sleep(2)
#     products_page = ProductsPage(driver)
#     products_page.test_dashboard_products_click()
#     time.sleep(2)
#     assert products_page.test_Products_Visible()
#
# #test-case to test for Groups-Menu visible or not
# def test_GroupsMenu():
#     time.sleep(2)
#     groups_page = GroupsPage(driver)
#     groups_page.test_dashboard_groups_click()
#     time.sleep(2)
#     assert groups_page.test_Groups()
#
# #test-case to test for Users-Menu visible or not
# def test_UsersMenu():
#     time.sleep(2)
#     users_page = UsersPage(driver)
#     users_page.test_dashboard_usersmenu_click()
#     time.sleep(2)
#     assert users_page.test_Users()
#
# #test-case to test for Farmers-Menu visible or not
# def test_FarmersMenu():
#     time.sleep(2)
#     farmers_page = FarmersPage(driver)
#     farmers_page.test_dashboard_farmersmenu_click()
#     time.sleep(2)
#     assert farmers_page.test_members_farmersmenu()
#
# #test-case to test for Harvest-Menu visible or not
# def test_HarvestsMenu():
#     time.sleep(2)
#     harvests_page = HarvestsPage(driver)
#     harvests_page.test_dashboard_harvests_click()
#     time.sleep(2)
#     assert harvests_page.test_Harvests()
#
# #test-case to test for Agri-input menu visible or not
# def test_AgriInputMenu():
#     time.sleep(2)
#     agriinput_page = AgriInputs(driver)
#     agriinput_page.test_dashboard_agriinput_click()
#     time.sleep(2)
#     assert agriinput_page.CheckForInputDemand()
#     driver.close()
































