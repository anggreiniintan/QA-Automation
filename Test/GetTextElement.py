from selenium import webdriver
import time

class GetText():
    def get_text(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        driver = webdriver.Chrome(executable_path = path)

        driver.get("https://www.yatra.com/")
        driver.implicitly_wait(5)

        elementt = driver.find_element_by_xpath("//*[@id='themeSnipe']/section/div[2]/div[5]/div/h1")
        driver.implicitly_wait(5)

        print(elementt.text)
        time.sleep(4)

gt = GetText()
gt.get_text()        

