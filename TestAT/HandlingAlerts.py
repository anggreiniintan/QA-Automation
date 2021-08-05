from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

option = Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")

# path = "C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(executable_path=r'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe')

driver.get("https://demoqa.com/alerts")
time.sleep(2)

driver.find_element_by_id("alertButton").click()
time.sleep(2)
#handling Alarets Pop-Up
driver.switch_to.alert.accept()