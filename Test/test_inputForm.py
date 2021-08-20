import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

class Testform():

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    CHOOSE_GENDER = (By.CSS_SELECTOR, ".custom-control-label")
    PHONE_NUMBER = (By.ID, "userNumber")
    DOB_COL = (By.ID, "dateOfBirthInput")
    SUBJ = (By.ID, "subjectsInput")
    
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
        print(choose_gender.is_selected)
        choose_gender.click()

        #input Phone Number
        phone_number = self.driver.find_element(*self.PHONE_NUMBER)
        phone_number.send_keys("09876543")

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
        time.sleep(5)

        #select year
        choose_year = self.driver.find_element_by_css_selector(".react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--select")
        choose_year.click()

        list_year = self.driver.find_element_by_class_name("react-datepicker__year-select")
        selected_to_year=Select(list_year)
        #choose year
        selected_to_year.select_by_visible_text("1997")
        time.sleep(5)

        #select date
        select_date = self.driver.find_elements_by_css_selector(".react-datepicker__day")
        for i in select_date:
            if i.text == "15":
                i.click()
                break
        
        #input Subjects
        subs = self.driver.find_element(*self.SUBJ)
        subs.send_keys("aaa") 

        #checklist Hobbies       



