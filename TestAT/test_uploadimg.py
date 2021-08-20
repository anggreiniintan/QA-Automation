
import time
from selenium import webdriver


class TestUpload():

    path_directory = "C://Users/USER/Documents/Scanned Documents/img.png"
    
    def setup_method(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)
        self.driver.get("https://demoqa.com/upload-download")

    def teardown_method(self):
        self.driver.quit()

    def test_upload(self):
        click_button = self.driver.find_element_by_id("uploadFile")
        click_button.send_keys(self.path_directory)
        time.sleep(5)
    
    def test_download(self):
        click_button = self.driver.find_element_by_id("downloadButton")
        click_button.click()