from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../drivers/chromedriver.exe")
# driver = webdriver.Firefox(r"C:\Users\giggl\PycharmProjects\LearnPythons\drivers\geckodriver.exe")
# driver = webdriver.Ie(r"C:\Users\giggl\PycharmProjects\LearnPythons\drivers\msedgedriver.exe")

driver.set_page_load_timeout("20")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

driver.maximize_window()
driver.refresh()

print("Test completed sucessfully")
time.sleep(4)
driver.quit()
