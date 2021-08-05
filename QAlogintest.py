from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")

path = "C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(executable_path = path)

driver.get("https://course.refactory.id")
print(driver.title)

link = driver.find_element_by_link_text("Login")
link.click()


try:
    element = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.ID, "user_email"))
    )
finally:
    driver.find_element_by_id("user_email").send_keys("anggreiniintn@gmail.com")
    driver.find_element_by_id("user_password").send_keys("")
    driver.find_element_by_name("commit").click()
    

time.sleep(5)
