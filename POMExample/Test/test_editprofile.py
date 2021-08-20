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
    
  def test_edit_data_check_valid(self, browser: webdriver.Remote):
    edit_profile = TestEditProfile()
    edit_profile_page = EditProfile(browser)
    edit_profile.test_edit_profile_valid(browser)

    try:
        edit_profile_page.get_first_name()
    finally: 
        get_text = edit_profile_page.get_first_name()
        print(get_text)
        assert get_text == "Anggreini Intan Permata"

    try:
        edit_profile_page.get_last_name()
    finally: 
        get_text = edit_profile_page.get_last_name()
        print(get_text)
        assert get_text == "Sari"

    try:
        edit_profile_page.get_phone_numb()
    finally: 
        get_text = edit_profile_page.get_phone_numb()
        print(get_text)
        assert get_text == "08123456789"

    try:
        edit_profile_page.get_date_picker()
    finally: 
        get_text = edit_profile_page.get_date_picker()
        print(get_text)
        assert get_text == "2021-06-15"

    try:
        edit_profile_page.get_gender()
    finally: 
        get_text = edit_profile_page.get_gender()
        print(get_text)
        assert get_text == "Wanita"

    try:
        edit_profile_page.get_city()
    finally: 
        get_text = edit_profile_page.get_city()
        print(get_text)
        assert get_text == "Kab. Sleman"

    try:
        edit_profile_page.get_desc()
    finally: 
        get_text = edit_profile_page.get_desc()
        print(get_text)
        assert get_text == "BIO"

  def test_change_photo_profile(self, browser: webdriver.Remote):
    testdashboard_page = TestDashboard()
    edit_profile_page = EditProfile(browser)
    testdashboard_page.test_click_editprofile(browser)