from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DashboardPage():
    USER_INFO = (By.XPATH, "//*[@id='dashboard']/aside/nav/ul/li[1]/div/div/h4")
    DROPDOWN_PROFILE_HEADER = (By.XPATH, "//*[@id='header']/div[1]/div/div/div[1]/ul/li[5]")
    DROPDOWN_MENU =(By.ID, "profile-menu")
    EDIT_PROFILE_MENU = (By.LINK_TEXT, "Edit Profile")

    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    def get_user_info(self):
        user_info = WebDriverWait(self.driver, 30000).until(
            EC.presence_of_element_located(self.USER_INFO))
        return user_info.text

    def profile_header_click(self):
        profile_click = self.driver.find_element(*self.DROPDOWN_PROFILE_HEADER)
        profile_click.click()
    
    def click_menu_dropdown(self):
        self.driver.implicitly_wait(5)
        menu_dropdown = self.driver.find_element(*self.DROPDOWN_MENU)
        menu_dropdown_value = menu_dropdown.find_element(*self.EDIT_PROFILE_MENU)
        menu_dropdown_value.click()
    
    