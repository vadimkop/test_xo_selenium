from selenium.webdriver.common.by import By


class SearchLocators:

    WHERE_FROM = (By.CSS_SELECTOR, "#leg-1-from")
    WHERE_TO = (By.CSS_SELECTOR, "#leg-1-to")

    LIST_NEARBY = (By.ID, "UDYZ")
    LIST_TO = (By.ID, "LPPT")

    BUTTON_SEARCH = (By.CSS_SELECTOR, "div._fB > button")

    AIR_CLASS_HEAVY = (By.CSS_SELECTOR, "button:nth-child(5)")
    SELECTED_CLASS = (By.CSS_SELECTOR, "div._Dg > button")

    PRESENT_DAY = (By.CSS_SELECTOR, "button._CT._ET")


class LoginLocators:

    MODAL_LOGIN = (By.ID, "modal-header")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login__button")
    LOGIN_ERROR = (By.CLASS_NAME, "field__error")


