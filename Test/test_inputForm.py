import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Testform():

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    CHOOSE_GENDER = (By.CSS_SELECTOR, ".custom-control-label")
    PHONE_NUMBER = (By.ID, "userNumber")
    DOB_COL = (By.ID, "dateOfBirthInput")
    SUBJ = (By.ID, "subjectsInput")
    CHECK_BOX1 = (By.ID, "hobbies-checkbox-1")
    CHECK_BOX2 = (By.ID, "hobbies-checkbox-2")
    CHECK_BOX3 = (By.ID, "hobbies-checkbox-3")
    UPLOAD =(By.ID, "uploadPicture")
    ADDRESS = (By.ID, "currentAddress")
    STATE= (By.ID, "state")
    INPUT_STATE = (By.ID, "react-select-3-input")
    CITY = (By.ID, "city")
    INPUT_CITY = (By.ID, "react-select-4-input")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "#submit.btn.btn-primary")
    TITTLE_TEXT = (By.ID, "example-modal-sizes-title-lg")

    path_directory = "C://Users/USER/Documents/Scanned Documents/img.png"
    
    
    def setup_method(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)
        self.driver.get("https://demoqa.com/automation-practice-form")

    def teardown_method(self):
        self.driver.quit()
    
    def test_inputForm(self):
    
        #input Name
        first_name = self.driver.find_element(*self.FIRST_NAME)
        last_name = self.driver.find_element(*self.LAST_NAME)
        first_name.send_keys("Anggreini Intan")
        last_name.send_keys("Sari")

        #input Email
        email = self.driver.find_element(*self.EMAIL)
        email.send_keys("blabla@gmail.com")
        
        #choose Gender
        choose_gender = self.driver.find_element(*self.CHOOSE_GENDER)
        choose_gender.click()

        #input Phone Number
        phone_number = self.driver.find_element(*self.PHONE_NUMBER)
        phone_number.send_keys("0987654987")

        #choose Date of Birth
        dob_col = self.driver.find_element(*self.DOB_COL)
        dob_col.click()

        #select month
        choose_month = self.driver.find_element_by_css_selector(".react-datepicker__month-dropdown-container.react-datepicker__month-dropdown-container--select")
        choose_month.click()

        list_month = self.driver.find_element_by_class_name("react-datepicker__month-select")
        selected_to_month=Select(list_month)
        #choose month
        selected_to_month.select_by_visible_text("May")
        time.sleep(2)

        #select year
        choose_year = self.driver.find_element_by_css_selector(".react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--select")
        choose_year.click()

        list_year = self.driver.find_element_by_class_name("react-datepicker__year-select")
        selected_to_year=Select(list_year)
        #choose year
        selected_to_year.select_by_visible_text("1997")
        time.sleep(2)

        #select date
        select_date = self.driver.find_elements_by_css_selector(".react-datepicker__day")
        for i in select_date:
            if i.text == "15":
                i.click()
                break
        
        #input Subjects
        subs = self.driver.find_element(*self.SUBJ)
        subs.send_keys("Math") 
        subs.send_keys(Keys.DOWN)
        subs.send_keys(Keys.ENTER)

        subs.send_keys("Accounting") 
        subs.send_keys(Keys.DOWN)
        subs.send_keys(Keys.ENTER)

        #checklist Hobbies     
        self.driver.execute_script("window.scrollTo(0, 150)") 
        time.sleep(3)  
        check_box1 = self.driver.find_element(*self.CHECK_BOX1)
        check_box2 = self.driver.find_element(*self.CHECK_BOX2)        
        check_box3 = self.driver.find_element(*self.CHECK_BOX3)

        self.driver.execute_script('arguments[0].click()', check_box1)
        self.driver.execute_script('arguments[0].click()', check_box2)
        self.driver.execute_script('arguments[0].click()', check_box3)        

        #upload pict 
        upload_img = self.driver.find_element(*self.UPLOAD)
        upload_img.send_keys(self.path_directory)

        #input Current Address
        current_add = self.driver.find_element(*self.ADDRESS)
        current_add.send_keys("jl. dfgtyuikjbvvb")

        #select state and city
        #choose state
        self.driver.execute_script("window.scrollTo(0, 350)") 
        select_state = self.driver.find_element(*self.STATE)
        select_state.click()
        input_state = self.driver.find_element(*self.INPUT_STATE)       
        input_state.send_keys("NCR")
        input_state.send_keys(Keys.DOWN)
        input_state.send_keys(Keys.ENTER)

        #choose city
        select_city = self.driver.find_element(*self.CITY)
        select_city.click()
        input_state.send_keys("Delhi")
        input_state.send_keys(Keys.DOWN)
        input_state.send_keys(Keys.ENTER)

        #click button
        button_submit = self.driver.find_element(*self.BUTTON_SUBMIT)
        self.driver.execute_script('arguments[0].click()', button_submit)

        time.sleep(5)

        #validation
        tittle_text = self.driver.find_element(*self.TITTLE_TEXT)
        time.sleep()
        assert tittle_text.text == "Thanks for submitting the form"

