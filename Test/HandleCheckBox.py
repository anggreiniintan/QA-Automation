from selenium import webdriver
import time

class HandleCheckBox():
    def handle_checkbox(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        driver = webdriver.Chrome(executable_path = path)

        driver.get("https://sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        
        driver.find_element_by_id("interest_market_c0").click()
        time.sleep(5)
        # after clicking, verifed checkbox has been selected succesfully.
        ver1 = driver.find_element_by_id("interest_market_c0").is_selected()
        print(ver1)
                
        # driver.find_element_by_id("interest_sell_c0").click()
        
        ver2 = driver.find_element_by_id("interest_sell_c0").is_selected()
        print(ver2)

        ver3 = driver.find_element_by_id("interest_serve_c0").is_selected()
        print(ver3)
        time.sleep(5)


    
hcb = HandleCheckBox()
hcb.handle_checkbox()