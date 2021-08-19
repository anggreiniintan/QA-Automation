from selenium import webdriver

path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)

driver.implicitly_wait(4)

driver.get("https://www.idntimes.com/news")

# def test_headline():
#     headline = driver.find_element_by_class_name("side-headline")
#     box_headline = headline.find_elements_by_class_name("box-panel")
#     assert len(box_headline) == 5
    
# def test_news():
#     trendingNews = driver.find_element_by_class_name("list-trending")
#     box_trending = trendingNews.find_elements_by_class_name("box-panel")
#     # box = box_trending.find_elements_by_class_name("box-panel")
#     assert print(len(box_trending))


# def test_count_article():
#     artikel = driver.find_element_by_id("latest-article")
#     box_ar = artikel.find_elements_by_class_name("box-latest")
#     assert len(box_ar) == 18

def dropdownn():
    drop = driver.find_element_by_class_name("dropdown-menu-list-header")
    submenu = drop.find_element_by_class_name("dropdown-submenu-header")
    box_submenu = submenu.find_element_by_class_name("submenu-box")
    title = box_submenu.find_elements_by_tag_name("a")
    assert print(title.text)


