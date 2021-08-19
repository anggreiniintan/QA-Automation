from selenium import webdriver
import pytest

path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)

def setup_method(self):
    
    driver.get('https://www.idntimes.com/news')
   

# def teardown_method(self):
#     driver.quit()

# def testtttttsas(self):
#     driver.get('https://www.idntimes.com/news')
        