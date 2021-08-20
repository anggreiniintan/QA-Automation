from selenium import webdriver
import pytest


path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)

#skenario
Kunci = [
    ("rizkaelni", "RizkaElni21"),    #username benar pw salah
    ("rizkaeln", "RizkaElni21@"),    #username salah pw benar
    ("rizkaeln", "RizkaEli21@")      #username salah pw salah
    # ("","RizkaElni21"),              #username kosong pw benar
    # ("rizkaelni", ""),               #username benar pw kosong
    # ("","")                          #username kosong pw kosong
    # ("rizkaelni", "RizkaElni21@")  #username benar pw benar
]  

driver.minimize_window()
driver.implicitly_wait(4)

@pytest.mark.parametrize('a,b', Kunci)
def test_login(a,b):
    driver.get("https://demoqa.com/login")
    driver.find_element_by_id("userName").send_keys(a)
    driver.find_element_by_id("password").send_keys(b)
    driver.find_element_by_id("login").click()

    
    driver.implicitly_wait(4)
    invalidText = driver.find_element_by_id("name").text

    assert invalidText == "Invalid username or password!"

