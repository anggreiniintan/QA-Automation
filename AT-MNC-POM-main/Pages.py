from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from TestData import TestData
from Locators import Locators


class BasePage:
    def __init__(self, driver):
        # driver = 'C:/Note/Scripts/chromedriver_win32 (1)/chromedriver.exe'
        self.driver = driver
        self.action = ActionChains(driver)

    # function input data
    def enter_text(self, locator, teks):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(teks)

    # Fungsi Klick Locator
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    # Fungsi hapus data
    def clear_text(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).clear()

    # Fungsi ambil text
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

    def get_toast(self, locator):
        get_toast = self.driver.find_element(locator)
        return get_toast.get_attribut("innerHTML")

    # fungsi_cek_elementvisible
    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False

            # fungsi select dropdown

    def select_dropdown_by_value(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_value(item)

    def select_dropdown_by_visible_text(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_visible_text(item)

    # fungsi hover
    def move_element_to(self, locator):
        hover = self.driver.find_element_by_xpath(locator)
        self.action.move_to_element(hover).perform()

    # FUNGSI click js alert
    def alert_click(self, locator):
        self.driver.find_element_by_xpath(locator).click()
        self.driver.switch_to.alert.accept()


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login_valid(self):
        # type email
        self.enter_text(Locators.EMAIL_FIELD, TestData.SIGN_IN_EMAIL)
        self.click(Locators.NEXT_BUTTON)
        self.enter_text(Locators.PASSWORD_FIELD, TestData.SIGN_IN_PASSWORD)
        self.click(Locators.SIGN_IN_BUTTON)

    def emailEmpty(self):
        self.click(Locators.NEXT_BUTTON)

    def email_invalid(self):
        self.enter_text(Locators.EMAIL_FIELD, TestData.SIGN_IN_EMAIL_INVALID)
        self.click(Locators.NEXT_BUTTON)

    def email_not_registered(self):
        self.enter_text(Locators.EMAIL_FIELD, TestData.SIGN_IN_EMAIL_NOT_REGISTERED)
        self.click(Locators.NEXT_BUTTON)

    def password_empty(self):
        self.enter_text(Locators.EMAIL_FIELD, TestData.SIGN_IN_EMAIL)
        self.click(Locators.NEXT_BUTTON)
        self.click(Locators.SIGN_IN_BUTTON)

    def password_invalid(self):
        self.enter_text(Locators.EMAIL_FIELD, TestData.SIGN_IN_EMAIL)
        self.click(Locators.NEXT_BUTTON)
        self.enter_text(Locators.PASSWORD_FIELD, TestData.SIGN_IN_PASSWORD_INVALID)
        self.click(Locators.SIGN_IN_BUTTON)

    def password_invalid_to_many_entered(self):
        self.enter_text(Locators.EMAIL_FIELD, TestData.SIGN_IN_EMAIL)
        self.click(Locators.NEXT_BUTTON)
        # 1
        self.enter_text(Locators.PASSWORD_FIELD, TestData.SIGN_IN_PASSWORD_INVALID)
        self.click(Locators.SIGN_IN_BUTTON)
        self.clear_text(Locators.PASSWORD_FIELD)
        # 2
        self.enter_text(Locators.PASSWORD_FIELD, TestData.SIGN_IN_PASSWORD_INVALID)
        self.click(Locators.SIGN_IN_BUTTON)
        self.clear_text(Locators.PASSWORD_FIELD)
        # 3
        self.enter_text(Locators.PASSWORD_FIELD, TestData.SIGN_IN_PASSWORD_INVALID)
        self.click(Locators.SIGN_IN_BUTTON)
        self.clear_text(Locators.PASSWORD_FIELD)
        # 4
        self.enter_text(Locators.PASSWORD_FIELD, TestData.SIGN_IN_PASSWORD_INVALID)
        self.click(Locators.SIGN_IN_BUTTON)
        self.clear_text(Locators.PASSWORD_FIELD)








class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    def update_fullname(self):
        self.is_visible(Locators.PROFILE_ICON_BUTTON)
        self.click(Locators.PROFILE_ICON_BUTTON)
        self.clear_text(Locators.PRO_FULL_NAME_FIELD)
        self.enter_text(Locators.PRO_FULL_NAME_FIELD, TestData.PRO_FULL_NAME)
        self.click(Locators.PRR_UPDATE_MANAGE_PROFILE)


class MerchantPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def merchant_detail(self):
        self.click(Locators.MERCHANT_MENU)
