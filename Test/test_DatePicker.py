from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

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
        selected_to_month.select_by_visible_text("February")

        select_year = self.driver.find_element_by_class_name("react-datepicker__year-select")
        select_year.click()

        selected_to_year=Select(select_year)
        selected_to_year.select_by_visible_text("2021")

        select_date = self.driver.find_elements_by_css_selector(".react-datepicker__day")
        for i in select_date:
            if i.text == "24":
                i.click()
                break
       

        
        
        
        
