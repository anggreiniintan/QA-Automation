from selenium import webdriver

path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)

driver.implicitly_wait(4)

driver.get("https://www.idntimes.com/news")
tittlee = driver.title
assert tittlee == "IDN"