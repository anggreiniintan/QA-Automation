from selenium import webdriver
from Pages.editprofile_page import EditProfile
from Test.test_login import TestLogin
from Pages.dashboard_page import DashboardPage


class TestDashboard():
    def test_click_editprofile(self, browser: webdriver.Remote):
        login_page = TestLogin()
        dashboard_page = DashboardPage(browser)
        edit_profile_page = EditProfile(browser)
        login_page.test_valid_login(browser)
        dashboard_page.profile_header_click()
        dashboard_page.click_menu_dropdown()

        # assert edit_profile_page.get_title == "Save Profile"
    
  
        