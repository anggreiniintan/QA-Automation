from selenium import webdriver

path = "C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(executable_path = path)

driver.get("https://the-internet.herokuapp.com/")

driver.maximize_window()

# driver.minimize_window()