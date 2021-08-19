from selenium import webdriver

class TestEditProfile():
    __test__ = False
    def setup_method(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)
        self.driver.get("https://community.idntimes.com/login")

    def test_login(self):
        self.driver.find_element_by_xpath("//*[@id='signin']/div[1]/form/div[1]/input").send_keys("anggreiniintn@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='signin']/div[1]/form/div[2]/input").send_keys("123456789")
        self.driver.find_element_by_xpath("//*[@id='signin']/div[1]/form/button").click()

        # self.driver.find_element_by_xpath("//*[@id='profile-menu'']/li[2]/a").click()

    
    # def teardown_method(self):
    #     self.driver.quit()

    # def entry_editprofile(self):
    #     self.driver.find_element_by_id("first_name").send_keys("Anggreini Intan Permata")

