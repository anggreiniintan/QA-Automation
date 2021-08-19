from selenium import webdriver
import time

class TestNews():
    def setup_method(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)
        self.driver.get("https://community.idntimes.com/login")

    # def teardown_method(self):
    #     self.driver.quit()

    def test_login(self):
        self.driver.find_element_by_xpath("//*[@id='signin']/div[1]/form/div[1]/input").send_keys("anggreiniintn@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='signin']/div[1]/form/div[2]/input").send_keys("123456789")
        self.driver.find_element_by_xpath("//*[@id='signin']/div[1]/form/button").click()

        self.driver.find_element_by_xpath("//*[@id='profile-menu'']/li[2]/a").click()

    # def editprofile(self):
    #     self.driver.find_element_by_id("first_name").send_key("Anggreini Intan")


    # def test_tittle(self):
    #     tittlee = self.driver.title
    #     assert tittlee == "Berita Terki...a | IDN Times"

    # def testt_headline(self):
    #     headline = self.driver.find_element_by_class_name("side-headline")
    #     box_headline = headline.find_elements_by_class_name("box-panel")
    #     assert len(box_headline) == 5
        
    # def test_news(self):
    #     list_box = self.driver.find_element_by_css_selector(".list-trending")
    #     trendingNews = list_box.find_elements_by_css_selector(".slick-slide.slick-active")
    #     print(len(trendingNews))
    #     for i in trendingNews:
    #         print(i.text)

    # def test_count_articles(self):
    #     artikel = self.driver.find_element_by_id("latest-article")
    #     box_ar = artikel.find_elements_by_class_name("box-latest")
    #     assert len(box_ar) == 18

    # def test_dropdown(self): #positive case
    #     menu_components = ["IDN Times", "Jawa Barat", "Banten", "Jawa Tengah", "Jogja",
    #                     "Jawa Timur", "Bali", "Sumatera Utara", "Sulawesi Selatan",
    #                     "Kalimantan Timur", "Sumatera Selatan", "Lampung", "NTB"]
    
    #     menu_box = self.driver.find_elements_by_css_selector("ul.dropdown-menu-regional a")
    #     print(len(menu_box))
        
    #     for i in menu_box:
    #         print("menu : %s" % i.get_attribute("innerText"))
    #         assert i.get_attribute("innerText") in menu_components
    
    # def test_dropdown_negatif(self): #negatif case
    #     menu_components = ["IDN Times", "Jawa Barat", "Banten", "Jawa Tengah", "Jogja",
    #                     "Jawa Timur", "Bali", "Sumatera Utara", "Sulawesi Selatan",
    #                     "Kalimantan Timur", "Sumatera Selatan", "", ""]
        
    #     menu_box = self.driver.find_elements_by_css_selector("ul.dropdown-menu-regional a")
    #     print(len(menu_box))
        
    #     for i in menu_box:
    #         print("menu : %s" % i.get_attribute("innerText"))
    #         assert i.get_attribute("innerText") in menu_components
    
    # def test_counting(self):
    #     box_information = self.driver.find_element_by_css_selector(".left-content")
    #     box_count = box_information.find_elements_by_css_selector("h1")
        
    #     # print(box_information.get_attribute("innerText"))
    #     print(len(box_count))
    #     for i in box_count:
    #       assert  i.text == "Kejatuhan Kunduz, Ini 3 Fakta Kota Benteng Tua Afghanistan"
        # assert box_information == 3
