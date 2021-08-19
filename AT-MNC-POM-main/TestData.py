from faker import Faker


class TestData:
    fake = Faker(["id_ID"])

    BASE_URL = "https://staging-partner-explore.misterb2b.com/login"

    # Email SIgn in
    SIGN_IN_EMAIL = ''
    SIGN_IN_EMAIL_INVALID = 'misteraladinqa_gmail.com'
    SIGN_IN_EMAIL_NOT_REGISTERED = 'egaqarf@gmail.com'
    SIGN_IN_PASSWORD = ''
    SIGN_IN_PASSWORD_INVALID = '@Mis'
    TOAST_LOGIN_SUCCESS_DATA = "Logging in"
    ALERT_EMAIL_EMPTY_DATA = "Enter your email address to continue"
    ALERT_EMAIL_INVALID_DATA = "That email address isn't correct"
    ALERT_EMAIL_NOT_REGISTERED = "Not Authorized"
    ALERT_PASSWORD_EMPTY_DATA = 'Enter your password'
    ALERT_PASSWORD_INVALID = "The email and password you entered don't match"

    # PROFILE
    PRO_FULL_NAME = fake.name()
    PRO_TOAST_FN_DATA = "Success change fullname"
    MERCHANT_PAGE_TITLE_DATA = 'Merchant Detail'
    MER_CONTACT_DETAIL_COMPANY_DATA = 'Contact Detail Company'
    MER_CONTACT_DETAIL_PIC_DATA = 'Contact Detail PIC'
    MER_BANK_ACCOUNT_DATA = 'Contact Detail PIC'





