from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
driver.find_element_by_id("timerAlertButton").click()

try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    time.sleep(3)
    driver.switch_to.alert.accept()
    print("alart accept")
except TimeoutException:
    print("alrt melebihi 10 detik")
    pass
