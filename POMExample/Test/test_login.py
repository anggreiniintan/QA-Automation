from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.dashboard_page import DashboardPage

class TestLogin():
    def test_valid_login(self, browser: webdriver.Remote):
        dashboard_page = DashboardPage(browser)
        login_page = LoginPage(browser)
        login_page.load_website()
        login_page.set_email("anggreiniintn@gmail.com")
        login_page.set_pw("123456789")
        login_page.button_signin_click()

        assert dashboard_page.get_user_info() == "Anggreini Intan Permata Sari"

    def test_wrong_email(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)
        login_page.load_website()
        login_page.set_email("anggreini@gmail.com")
        login_page.set_pw("123456789")
        login_page.button_signin_click()

        assert login_page.wrong_email() == "Oops.. sorry email kamu belum terdaftar, nih!"

    def test_wrong_pw(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)
        login_page.load_website()
        login_page.set_email("anggreiniintn@gmail.com")
        login_page.set_pw("12")
        login_page.button_signin_click()

        assert login_page.wrong_pw() == "Password kamu tidak sesuai, kamu lupa?"

    def test_email_null(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)
        login_page.load_website()
        login_page.set_email("")
        login_page.set_pw("123456789")
        login_page.button_signin_click()        

        assert login_page.email_null() == "Please fill out this field"

    def test_pw_null(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)
        login_page.load_website()
        login_page.set_email("anggreiniintn@gmail.com")
        login_page.set_pw("")
        login_page.button_signin_click()        

        assert login_page.pw_null() == "Please fill out this field"
    
    def test_emailpw_null(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)
        login_page.load_website()
        login_page.set_email("")
        login_page.set_pw("")
        login_page.button_signin_click()        

        assert (login_page.email_null() and login_page.pw_null()) == "Please fill out this field"