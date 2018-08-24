from selenium import webdriver


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, options=options)
driver.get("http://35.154.213.24")


