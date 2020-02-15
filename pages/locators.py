from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    USER_NAME = (By.NAME, "login-username")
    REG_EMAIL = (By.NAME, "registration-email")


class ProductPageLocators:
    CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_INFO = (By.CSS_SELECTOR, ".product_main")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p")
