from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

option = Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")

# path = "C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(executable_path=r'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe')


driver.get("https://demoqa.com/alerts")
time.sleep(2)


try:
    element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.ID, "alertButton"))
    )
finally: 
    #handling Alarets Pop-Up for one button click
    driver.find_element_by_id("alertButton").click()
    time.sleep(5)
    driver.switch_to.alert.accept()

try:
    element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.ID, "confirmButton"))
    )
finally: 
    #handling Alarets Pop-Up for two button click and select button OK
    driver.find_element_by_id("confirmButton").click()
    time.sleep(5)
    driver.switch_to.alert.accept()    

try:
    element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.ID, "confirmButton"))
    )
finally: 
    #handling Alarets Pop-Up for two button click and select button Cancel
    driver.find_element_by_id("confirmButton").click()
    time.sleep(5)
    driver.switch_to.alert.dismiss()    


