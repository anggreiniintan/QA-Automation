from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized") 

path = "C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(executable_path = path)

driver.get("https://tees.co.id/")

try:
    element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]'))
    )
    print("Pop Up Muncul")    
finally: 
    time.sleep(4)
    driver.find_element_by_class_name("btn-modal-close").click()
    print("Pop Up Close") 

# except TimeoutException:
#     print("Pop Up Tidak Muncul ")
#     pass