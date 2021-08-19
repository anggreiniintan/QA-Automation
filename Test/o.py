from selenium import webdriver

path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)

driver.implicitly_wait(4)

def test_count_card():
    driver.get("https://www.idntimes.com/news")
    artikel = driver.find_element_by_id("latest-article")
    box_ar = artikel.find_elements_by_class_name("box-latest")

    assert len(box_ar) == 18