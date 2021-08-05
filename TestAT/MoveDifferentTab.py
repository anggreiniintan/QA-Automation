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

driver.get("https://the-internet.herokuapp.com/windows")
print(driver.title)
time.sleep(2)

driver.find_element_by_link_text("Click Here").click()
time.sleep(2)

# move to previouse tab
driver.switch_to_window(driver.window_handles[0]) 