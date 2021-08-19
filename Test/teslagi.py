from selenium import webdriver
import pytest

class Testtt() :
    def setup_method(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)

    def teardown_method(self):
        self.driver.quit()

    def testtttttsdsd(self):
        self.driver.get('https://www.idntimes.com/news')
        side_news = self.driver.find_element_by_id('latest-article')
        box_news = side_news.find_elements_by_class_name('box-latest')
        assert len(box_news) == 18
 