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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group>a")


class CartPageLocators:
    EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p[contains(text(), 'Your basket is empty')]")
    GOODS_LINK = (By.CSS_SELECTOR, ".basket-title")
