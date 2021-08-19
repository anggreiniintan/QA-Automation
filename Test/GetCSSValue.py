from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("start-maximized") 

class GetCssValue():
    def get_cssValue(self):
        path = "C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe"
        driver = webdriver.Chrome(executable_path = path)

        driver.get("https://saucedemo.com/")
        driver.implicitly_wait(5)

        link = driver.find_element_by_id("login_credentials")
        driver.implicitly_wait(5)

        print(link.value_of_css_property("line-height"))

gs = GetCssValue()
gs.get_cssValue()