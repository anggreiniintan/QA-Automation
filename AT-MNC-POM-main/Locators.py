from selenium.webdriver.common.by import By


class Locators:
    # LOGIN
    EMAIL_FIELD = (By.XPATH, "//input[@id='ui-sign-in-email-input']")
    PASSWORD_FIELD = (By.NAME, "password")
    FORGOT_PASSWORD = (By.XPATH, "//span[contains(text(),'click here')]")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".mdl-button--colored")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign In')]")
    ALERT_EMAIL_EMPTY = (By.XPATH, "//p[contains(text(),'Enter your email address to continue')]")
    ALERT_EMAIL_INVALID = (By.CSS_SELECTOR, ".firebaseui-id-email-error")
    ALERT_EMAIL_NOT_REGISTERED = (By.XPATH, "//h1[contains(text(),'Not Authorized')]")
    ALERT_PASSWORD_EMPTY = (By.XPATH, "//p[contains(text(),'Enter your password')]")
    ALERT_PASSWORD_INVALID = (By.CSS_SELECTOR, ".firebaseui-id-password-error")

    TOAST_LOGIN_SUCCESS = (By.XPATH, "//body/div[3]/div[3]/div[1]/div[1]/div[1]")

    # Profile
    PROFILE_ICON_BUTTON = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/*[1]")
    PRO_FULL_NAME_FIELD = (By.ID, "full-name")
    PRO_OLD_PASSWORD_FIELD = (By.ID, "old-password")
    PRO_NEW_PASSWD_FIELD = (By.ID, "new-password")
    PRO_CONFIRM_PASSWORD_FIELD = (By.ID, "confirm-new-password")
    PRR_UPDATE_MANAGE_PROFILE = (By.CSS_SELECTOR, "button.border.rounded.transition-colors")
    PRO_UPDATE_CHANGE_PASSWD_BTN =(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
    PROF_TOAST_UPDATE_FN = (By.XPATH, "//body/div[3]/div[3]/div[1]/div[1]/div[1]")

    # Merchant
    MERCHANT_MENU = (By.XPATH, "//span[contains(text(),'Merchant')]")
    MERCHANT_PAGE_TITLE = (By.XPATH, "// div[contains(text(), 'Merchant Detail')]")
    MER_CONTACT_DETAIL = (By.XPATH, "//div[contains(text(),'Contact Detail Company')]")
    MER_CONTACT_DETAIL_PIC = (By.XPATH, "//div[contains(text(),'Contact Detail PIC')]")
    MER_BANK_ACCOUNT = (By.XPATH, "//div[contains(text(),'Contact Detail PIC')]")