from selenium import webdriver

class DropDown():
    def drop_down(self):
        path = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        driver = webdriver.Chrome(executable_path = path)

        driver.get("https://salesforce.com/ap/form/sem/crm-demo_b/?d=7010M00000220LlQAI&nc=7010M0000021hNSQAY&DCMP=KNC-Google&Brand=yes&ef_id=Cj0KCQjwu7OIBhCsARIsALxCUaP_NCzc6DNRJrFYYRcv-Pn7mK3Bq-LA3XsRF7Hs2lNtP24b4tELBwcaAlu7EALw_wcB:G:s&s_kwcid=AL!4720!3!421698520683!e!!g!!salesforce&gclid=Cj0KCQjwu7OIBhCsARIsALxCUaP_NCzc6DNRJrFYYRcv-Pn7mK3Bq-LA3XsRF7Hs2lNtP24b4tELBwcaAlu7EALw_wcB")
        driver.maximize_window()
