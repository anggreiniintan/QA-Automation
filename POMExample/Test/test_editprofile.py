from selenium import webdriver
from Pages.editprofile_page import EditProfile
from Test.test_login import TestLogin
from Test.test_dashboard import TestDashboard

class TestEditProfile():   
  def test_edit_valid_condition(self, browser: webdriver.Remote):
        testdashboard_page = TestDashboard()
        edit_profile_page = EditProfile(browser)
        testdashboard_page.test_click_editprofile(browser)

        edit_profile_page.clear_field_first_name()
        edit_profile_page.set_first_name("Anggreini Intan Permata")
        edit_profile_page.clear_field_last_name()
        edit_profile_page.set_last_name("Sari")
        edit_profile_page.clear_field_phone()
        edit_profile_page.set_phone_numb("08123456789")
        edit_profile_page.set_date_picker()
        edit_profile_page.choose_gender()
        edit_profile_page.choose_city()
        edit_profile_page.input_city("Sleman")
        edit_profile_page.input_desc("BIO")
        edit_profile_page.button_save_profile()

        assert edit_profile_page.succes_save() == "Profil Berhasil diperbaharui"
