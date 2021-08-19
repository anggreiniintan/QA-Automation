from selenium import webdriver
import time

class HandleRadioButton():
    def handle_radiobutton(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        driver = webdriver.Chrome(executable_path = path)

        driver.get("https://sugarcrm.com/au/request-demo/")
        driver.maximize_window()

        print(driver.find_element_by_id("doi0").is_selected())
        driver.find_element_by_id("doi0").click()
        print(driver.find_element_by_id("doi0").is_selected())
        time.sleep(4)
        
        print(driver.find_element_by_id("doi1").is_selected())
        time.sleep(4)
        driver.find_element_by_id("doi1").click()
        print(driver.find_element_by_id("doi1").is_selected())
        time.sleep(4)
    
    
hcb = HandleRadioButton()
hcb.handle_radiobutton()