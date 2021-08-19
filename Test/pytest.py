from selenium import webdriver

path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)

def tespytes():
    driver.get("https://www.google.com/")
    Title = driver.title

    assert Title == "Google"  #untuk melakukan validasi
