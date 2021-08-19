from selenium import webdriver
import time
import pytest
import requests
import urllib


path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)

driver.get("https://demoqa.com/login")
driver.find_element_by_id("newUser").click()
driver.implicitly_wait(3)

# driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()
# time.sleep(3)
# print(driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").is_selected())

#skenario
# Kunci = [
#     ("rizkaelni", "RizkaElni21"),    #username benar pw salah
#     ("rizkaeln", "RizkaElni21@"),    #username salah pw benar
#     ("rizkaeln", "RizkaEli21@")      #username salah pw salah
#     # ("","RizkaElni21"),              #username kosong pw benar
#     # ("rizkaelni", ""),               #username benar pw kosong
#     # ("","")                          #username kosong pw kosong
#     # ("rizkaelni", "RizkaElni21@")  #username benar pw benar
# ]  