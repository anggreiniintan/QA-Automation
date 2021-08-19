from os import times
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized") 

path = "C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(executable_path = path)

driver.get("https://demoqa.com/menu")
driver.maximize_window()

try:
    element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Main Item 2"))
    )
finally: 
    time.sleep(3)
    menu = driver.find_element_by_link_text("Main Item 2")
    Hover = ActionChains(driver).move_to_element(menu)
    Hover.perform()

try:
    element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sub Item"))
    )
finally: 
    time.sleep(3)
    menu = driver.find_element_by_link_text("Sub Item")
    Hover = ActionChains(driver).move_to_element(menu)
    Hover.perform()   
    
try:
    element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.LINK_TEXT, "SUB SUB LIST »"))
    )
finally: 
    time.sleep(3)
    menu = driver.find_element_by_link_text("SUB SUB LIST »")
    Hover = ActionChains(driver).move_to_element(menu)
    Hover.perform()    

try:
    element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Main Item 1"))
    )
finally: 
    time.sleep(3)
    menu = driver.find_element_by_link_text("Main Item 1")
    Hover = ActionChains(driver).move_to_element(menu)
    Hover.perform()

