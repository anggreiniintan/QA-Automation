from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditProfile():
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    EMAIL_INFO =(By.ID, "save-profile")
    PHONE = (By.ID, "phone_number")
    BIRTH_FIELD =(By.ID, "birth_date")
    DATE_PICKER = (By.CLASS_NAME, "datepicker-days")
    YEAR = (By.CLASS_NAME, "datepicker-switch")
    MONTH = (By.XPATH, "//*[@id='idntimes-desktop']/div[9]/div[2]/table/tbody/tr/td/span[6]")
    DAY = (By.XPATH, "//td[contains(text(),'15')]")
    GENDER = (By.XPATH, "//*[@id='profile-form']/div[6]/div/div[2]/input")
    RANDOM_PATH = (By.XPATH, "//*[@id='profile-form']/div[5]/label")
    CITY = (By.XPATH, "//*[@id='profile-form']/div[7]/span")
    INPUT_CITY =(By.CLASS_NAME, "select2-search__field")
    DESC = (By.ID, "description")
    BUTTON_SAVE = (By.ID, "save-profile")
    SEARCH_RESULT = (By.CSS_SELECTOR, "li.select2-results__option.select2-results__option--highlighted")
    SAVE_SUCCESS = (By.XPATH, "//div[contains(text(),'Profil Berhasil diperbaharui')]")
    FORM_EDIT = (By.ID, "profile-form")
    FORM_GROUP = (By.CLASS_NAME, "form-group" )
    GET_GENDER = (By.XPATH, "//*[@id='profile-form']/div[6]/div/div[2]/div")
    GET_INPUT_CITY = (By.NAME, "city")

    def __init__(self, browser: webdriver.Remote):
        self.driver = browser
    
    # def get_title(self):
    #     button = self.driver.find_element(*self.EMAIL_INFO)
    #     return button.text
    
    def clear_field_first_name(self):
        clear_field_FN = self.driver.find_element(*self.FIRST_NAME).clear()
        return clear_field_FN

    def clear_field_last_name(self):
        clear_field_LN = self.driver.find_element(*self.LAST_NAME).clear()
        return clear_field_LN
    
    def clear_field_phone(self):
        clear_field_Phone = self.driver.find_element(*self.PHONE).clear()
        return clear_field_Phone
    
    def clear_field_bio(self):
        clear_field_Bio = self.driver.find_element(*self.DESC).clear()
        return clear_field_Bio

    def set_first_name(self, first_name):
        first_namee = self.driver.find_element(*self.FIRST_NAME)
        first_namee.send_keys(first_name)
    
    def get_first_name(self):
        get_email_field = self.driver.find_element(*self.FIRST_NAME)
        return get_email_field.get_attribute("value")

    def set_last_name(self, last_name):
        last_namee = self.driver.find_element(*self.LAST_NAME)
        last_namee.send_keys(last_name)

    def get_last_name(self):
        get_last_namee = self.driver.find_element(*self.LAST_NAME)
        return get_last_namee.get_attribute("value")

    def set_phone_numb(self, phone):
        phone_number = self.driver.find_element(*self.PHONE)
        phone_number.send_keys(phone)

    def get_phone_numb(self):
        get_phone_number = self.driver.find_element(*self.PHONE)
        return get_phone_number.get_attribute("value")
    
    def set_date_picker(self):
        birth_date = self.driver.find_element(*self.BIRTH_FIELD)
        birth_date.click()
        find_date = self.driver.find_element(*self.DATE_PICKER)
        find_date.click()
        year = self.driver.find_element(*self.YEAR)
        year.click()
        month = self.driver.find_element(*self.MONTH)
        month.click()
        day = self.driver.find_element(*self.DAY)
        day.click()
        exit_date_picker = self.driver.find_element(*self.RANDOM_PATH)
        exit_date_picker.click()

    def get_date_picker(self):
        get_birth_date = self.driver.find_element(*self.BIRTH_FIELD)
        return get_birth_date.get_attribute("value")

    def choose_gender(self):
        gender = self.driver.find_element(*self.GENDER)
        gender.click()


    def get_gender(self):
        gender = self.driver.find_element(*self.GET_GENDER)
        return gender.text

    def choose_city(self):
        city = self.driver.find_element(*self.CITY)
        city.click()
    
    def input_city(self, city):
        inputC = self.driver.find_element(*self.INPUT_CITY)
        inputC.send_keys(city)
        box_result = WebDriverWait(self.driver, 3000).until(
            EC.presence_of_element_located(self.SEARCH_RESULT))
        box_result.click()
        
        # for i in box_result:
        #     print(len(i.text))


        # inputC.select_by_index(0) 
        # inputC.send_keys("ENTER")
        
    def get_city(self):
        getCity = self.driver.find_element(*self.GET_INPUT_CITY)
        return getCity.text
    
    def input_desc(self, desc):
        inputD = self.driver.find_element(*self.DESC)
        inputD.send_keys(desc)

    def get_desc(self):
        getDesc = self.driver.find_element(*self.DESC)
        return getDesc.text

    def button_save_profile(self):
        button_save_profile = self.driver.find_element(*self.BUTTON_SAVE)
        button_save_profile.click()
        
    def succes_save(self):
        succes_save_info = self.driver.find_element(*self.SAVE_SUCCESS)
        return succes_save_info.text

    def editForm(self):
        formEdit = self.driver.find_element(*self.FORM_EDIT)
        formGroup = formEdit.find_elements(*self.FORM_GROUP)
        return formGroup
        # for i in formGroup:
        #     return i
    
