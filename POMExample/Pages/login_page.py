from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class LoginPage():
    #LOCATOR
    EMAIL = (By.XPATH, "//*[@id='signin']/div[1]/form/div[1]/input")
    PASSWORD = (By.XPATH, "//*[@id='signin']/div[1]/form/div[2]/input")
    BUTTON_SIGIN = (By.XPATH, "//*[@id='signin']/div[1]/form/button")
    DASHBOARD_USERINFO = (By.XPATH, "//*[@id='dashboard']/aside/nav/ul/li[1]/div/div/h4")
    WRONG_INPUT_EMAIL = (By.XPATH, "//div[contains(text(),'Oops.. sorry email kamu belum terdaftar, nih!')]")
    WRONG_INPUT_PW = (By.XPATH, "//div[contains(text(),'Password kamu tidak sesuai, kamu lupa?')]")
    INPUT_EMAIL_NULL = (By.NAME, "email")
    INPUT_PW_NULL = (By.NAME, "password")
    
    #Method Constuctor
    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    def load_website(self):
        self.driver.get("https://community.idntimes.com/login")

    def set_email(self, email):
        email_field = self.driver.find_element(*self.EMAIL)
        email_field.send_keys(email)
    
    def set_pw (self, pw):
        pw_field = self.driver.find_element(*self.PASSWORD)
        pw_field.send_keys(pw)

    def button_signin_click(self):
        sigin_button = self.driver.find_element(*self.BUTTON_SIGIN)
        sigin_button.click()

    def get_userinfo_name(self):
        dashboard_username = self.driver.find_element(*self.DASHBOARD_USERINFO)
        return dashboard_username.text

    def wrong_email(self):
        wrong_inputEmail = self.driver.find_element(*self.WRONG_INPUT_EMAIL)
        return wrong_inputEmail.text
        
    def wrong_pw(self):
        wrong_inputPW = self.driver.find_element(*self.WRONG_INPUT_PW)
        return wrong_inputPW.text

    def email_null(self):
        email_inputNull = self.driver.find_element(*self.INPUT_EMAIL_NULL)
<<<<<<< HEAD
        return email_inputNull.text
    
    def pw_null(self):
        wrong_inputPW = self.driver.find_element(*self.INPUT_PW_NULL)
        return wrong_inputPW.text
=======
        return email_inputNull.get_attribute("validationMessage")
    
    def pw_null(self):
        wrong_inputPW = self.driver.find_element(*self.INPUT_PW_NULL)
        return wrong_inputPW.get_attribute("validationMessage")
>>>>>>> 7a8736b6484c2b77961a8a897e29ecf99b2972aa

    