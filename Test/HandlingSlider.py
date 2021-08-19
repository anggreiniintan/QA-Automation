from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class HandlingSlider():
    def handling_slider(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        driver = webdriver.Chrome(executable_path = path)

        driver.maximize_window()
        driver.get("https://www.snapdeal.com/search?keyword=mobile%20phone&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=ALL&url=&utmContent=&dealDetail=&sort=rlvncy")
        # driver.implicitly_wait(5)

        # slider1 = driver.find_element_by_xpath("//*[@id='content_wrapper']/div[7]/div[4]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[1]")    
        # slider2 = driver.find_element_by_xpath("//*[@id='content_wrapper']/div[7]/div[4]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[2]")

        try:
            WebDriverWait(driver, 6).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='content_wrapper']/div[7]/div[4]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[1]"))
            )
        finally: 
            slider1 = driver.find_element_by_xpath("//*[@id='content_wrapper']/div[7]/div[4]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[1]")
            ActionChains(driver).drag_and_drop_by_offset(slider1, 60, 0 ).perform()  #move x to y px
            time.sleep(5)

            produkTitle = driver.find_element_by_css_selector("p.product-title")
            print("Nama Produk :"+produkTitle.text)

        try:
            WebDriverWait(driver, 6).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='content_wrapper']/div[7]/div[4]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[2]"))
            )
        finally: 
            slider2 = driver.find_element_by_xpath("//*[@id='content_wrapper']/div[7]/div[4]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[2]")
            ActionChains(driver).drag_and_drop_by_offset(slider2, -20, 0 ).perform()  #move x to y px
            time.sleep(5)
            # dataMax = driver.find_element_by_tag_name

     

hs = HandlingSlider()
hs.handling_slider()