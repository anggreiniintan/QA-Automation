from selenium import webdriver


class TestNewsPage() :
    def setup_method(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path = path)

    def teardown_method(self):
        self.driver.quit()

    def test_count_headline_card(self):
        self.driver.get('https://www.idntimes.com/news')
        # side_panel = self.driver.find_element_by_class_name('side-headline')
        # box_panel = side_panel.find_elements_by_class_name('box-panel')
        # assert print(len(box_panel))

# note dr harlita: ntar jalaninnya tinggal pake pytest yak 