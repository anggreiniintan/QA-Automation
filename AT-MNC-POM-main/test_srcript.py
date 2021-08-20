from TestData import TestData
from Locators import Locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

from Pages import LoginPage
from Pages import ProfilePage
from Pages import MerchantPage


class BaseTest(unittest.TestCase):
    def setUp(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

# Login Page
class LoginTest(BaseTest):

    def test_email_password_valid(self):
        # Load Login
        self.login_page = LoginPage(self.driver)
        # Execute code
        self.login_page.login_valid()
        # assert
        register_info = self.login_page.get_text(Locators.TOAST_LOGIN_SUCCESS)
        self.assertEqual(TestData.TOAST_LOGIN_SUCCESS_DATA, register_info)
        time.sleep(3)

    def test_email_empty(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.emailEmpty()
        # assert
        alert_email = self.loginpage.get_text(Locators.ALERT_EMAIL_EMPTY)
        self.assertEqual(TestData.ALERT_EMAIL_EMPTY_DATA, alert_email)
        time.sleep(3)

    def test_email_invalid(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.email_invalid()

        alert_email_invalid = self.login_page.get_text(Locators.ALERT_EMAIL_INVALID)
        self.assertEqual(TestData.ALERT_EMAIL_INVALID_DATA, alert_email_invalid)
        time.sleep(3)

    def test_email_not_registered(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.email_not_registered()

        alert_email_not_registered = self.login_page.get_text(Locators.ALERT_EMAIL_NOT_REGISTERED)
        self.assertEqual(TestData.ALERT_EMAIL_NOT_REGISTERED, alert_email_not_registered)
        time.sleep(3)

    def test_password_empty(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.password_empty()
        # assert
        password_empty = self.login_page.get_text(Locators.ALERT_PASSWORD_EMPTY)
        self.assertEqual(TestData.ALERT_PASSWORD_EMPTY_DATA, password_empty)
        time.sleep(3)

    def test_password_invalid(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.password_invalid()
        # assert
        password_invalid = self.login_page.get_text(Locators.ALERT_PASSWORD_INVALID)
        self.assertEqual(TestData.ALERT_PASSWORD_INVALID, password_invalid)
        time.sleep(3)

    def test_password_invalid_enter(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.password_invalid_to_many_entered()



# Profile Page


class ProfileTest(BaseTest):
    def test_update_profile_valid(self):
        # login page
        self.login_page = LoginPage(self.driver)
        self.login_page.login_valid()
        time.sleep(7)
        # profile page
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.update_fullname()

        # assert
        toast_update = self.profile_page.get_text(Locators.PROF_TOAST_UPDATE_FN)
        self.assertEqual(TestData.PRO_TOAST_FN_DATA, toast_update)
        time.sleep(7)


# Merchant Page
class MerchantTest(BaseTest):
    def test_merchant_detail(self):
        # login page
        self.login_page = LoginPage(self.driver)
        self.login_page.login_valid()
        time.sleep(7)

        # merchant page
        self.merchant_page = MerchantPage(self.driver)
        self.merchant_page.merchant_detail()

        # assert page detail
        get_text_merchant = self.merchant_page.get_text(Locators.MERCHANT_PAGE_TITLE)
        self.assertEqual(TestData.MERCHANT_PAGE_TITLE_DATA, get_text_merchant)
        # detail company
        get_text_detail_company = self.merchant_page.get_text(Locators.MER_CONTACT_DETAIL)
        self.assertEqual(TestData.MER_CONTACT_DETAIL_COMPANY_DATA, get_text_detail_company)
        # detail pic
        get_text_detail_pic = self.merchant_page.get_text(Locators.MER_CONTACT_DETAIL)
        self.assertEqual(TestData.MER_CONTACT_DETAIL_COMPANY_DATA, get_text_detail_company)
        time.sleep(7)





