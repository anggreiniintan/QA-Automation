from selenium import webdriver
from Pages.editprofile_page import EditProfile
from Test.test_login import TestLogin
from Pages.dashboard_page import DashboardPage


class TestDashboard():
    def test_click_editprofile(self, browser: webdriver.Remote):
        login_page = TestLogin()
        dashboard_page = DashboardPage(browser)
        login_page.test_valid_login(browser)
        dashboard_page.profile_header_click()
        dashboard_page.click_menu_dropdown()

        # assert edit_profile_page.get_title == "Save Profile"

    def test_count_navbar(self, browser: webdriver.Remote):
        login_page = TestLogin()
        dashboard_page = DashboardPage(browser)
        login_page.test_valid_login(browser)

        menu_components = ["OLIMPIADE", "Tanya Jawab ", "NEWS", "BUSINESS", "SPORT",
                        "TECH", "HYPE", "LIFE", "HEALT", "COMMUNITY", "REGIONAL", "LAINNYA"]
        
        for i in dashboard_page.navbar():
           
            print("menu : %s" % i.text)
        
        # assert dashboard_page.navbar() == 13
        