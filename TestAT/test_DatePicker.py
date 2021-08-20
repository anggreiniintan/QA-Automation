from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys

class TestDatepicker():
    def setup_method(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)
        self.driver.get("https://demoqa.com/date-picker")

    def teardown_method(self):
        time.sleep(2)
        self.driver.quit()

    def test_date_picker(self):
       
        select_date = self.driver.find_element_by_id("datePickerMonthYearInput")
        select_date.click()

        select_month = self.driver.find_element_by_class_name("react-datepicker__month-select")
        select_month.click()

        selected_to_month=Select(select_month)
        selected_to_month.select_by_visible_text("May")

        select_year = self.driver.find_element_by_class_name("react-datepicker__year-select")
        select_year.click()

        selected_to_year=Select(select_year)
        selected_to_year.select_by_visible_text("2021")

        select_date = self.driver.find_elements_by_css_selector(".react-datepicker__day")
        for i in select_date:
            if i.text == "15":
                i.click()
                break
        
        value_datepicker = self.driver.find_element_by_id("datePickerMonthYearInput")
        value = value_datepicker.get_attribute("value")

        assert value == "02/24/2021"


    def test_date_time(self):
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 150)") 
        
        select_date_column = self.driver.find_element_by_id("dateAndTimePickerInput")
        select_date_column.click() 

        click_button_month = self.driver.find_element_by_class_name("react-datepicker__month-read-view--down-arrow")
        click_button_month.click()

        dropdown_month = self.driver.find_elements_by_css_selector(".react-datepicker__month-option")
        for i in dropdown_month:
            if i.text == "February":
                time.sleep(5)
                i.click()
                break

        click_button_year = self.driver.find_element_by_class_name("react-datepicker__year-read-view--down-arrow")
        click_button_year.click()

        dropdown_year = self.driver.find_elements_by_class_name("react-datepicker__year-read-view--down-arrow")
        for i in dropdown_year:
            if i.text == "2019":
                time.sleep(2)
                i.click()
                break
        
        select_date = self.driver.find_elements_by_class_name("react-datepicker__day")
        for i in select_date:
            if i.text == "28":
                time.sleep(5)
                i.click()
                break
        
        select_time = self.driver.find_elements_by_class_name("react-datepicker__time-list-item")
        for i in select_time:
            if i.text == "07:30":
                time.sleep(6)
                i.click()
                break

        
        assert select_date_column.get_attribute("value") == "February 28, 2021 7:30 AM"

        
