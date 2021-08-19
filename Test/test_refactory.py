from selenium import webdriver
import pytest
import time

class TestRizka():
    @pytest.fixture()
    def test_setup(rizka): 
        global driver   
        driver = webdriver.Chrome(executable_path="C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe")
        driver.get("https://www.demoblaze.com/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        time.sleep(3)
        driver.close()
        driver.quit()
        print("Test Completed") 
            
    def test_home(rizka, test_setup):
        driver.find_element_by_css_selector("#navbarExample > ul > li.nav-item.active > a").click()
        category = driver.find_element_by_id("cat")
        assert category.text == "Category"


    def test_Contact(rizka, test_setup):
        driver.find_element_by_css_selector("#navbarExample > ul > li:nth-child(2) > a").click()
        driver.find_elements_by_css_selector("#exampleModal > div > div")
        driver.find_element_by_id("recipient-email").send_keys("rizkaknisa@gmail.com")
        driver.find_element_by_id("recipient-name").send_keys("Rizka Khoirotunnisa")
        driver.find_element_by_id("message-text").send_keys("Haloo")
        driver.find_element_by_css_selector("#exampleModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        obj = driver.switch_to.alert
        setobj = obj.text
        time.sleep(2)
        obj.accept()
    
        assert  setobj == "a"
    


    def test_aboutUs(rizka, test_setup):
        #click 
        driver.find_element_by_css_selector("#navbarExample > ul > li:nth-child(3) > a").click()
        time.sleep(2)
        #play
        driver.execute_script('document.getElementsByTagName("video")[0].play()')
        time.sleep(2)
        #close
        driver.find_element_by_css_selector("#videoModal > div > div > div.modal-footer > button").click()

    def test_Cart(rizka, test_setup):
        driver.find_element_by_id("cartur").click()
        driver.find_element_by_css_selector("#page-wrapper > div > div.col-lg-1 > button").click()
        driver.find_element_by_id("name").send_keys("Rizka Khoirotunnisa")
        driver.find_element_by_id("country").send_keys("Indonesia")
        driver.find_element_by_id("city").send_keys("Palembang")
        driver.find_element_by_id("card").send_keys("abc")
        driver.find_element_by_id("month").send_keys("August")
        driver.find_element_by_id("year").send_keys("2021")
        driver.find_element_by_css_selector("#orderModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        time.sleep(3)    
        driver.find_element_by_css_selector("body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button").click()
        
    
    def testnegative_login(rizka, test_setup):
        driver.find_element_by_id("login2").click()
        driver.find_element_by_id("loginusername").send_keys("rizkaknisa")
        driver.find_element_by_id("loginpassword").send_keys("Rizka123")
        driver.find_element_by_css_selector("#logInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        time.sleep(5)
        obj = driver.switch_to.alert
        setobj = obj.text
        time.sleep(2)
        obj.accept()
    
        assert  setobj == "User does not exist."
    

        

        


        
 