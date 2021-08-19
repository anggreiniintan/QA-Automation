from selenium import webdriver

driver = webdriver.Chrome('C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe')

def tes_buka():
    driver.get('https://www.google.com/')
    Tittle = driver.title

    assert Tittle == "Google"