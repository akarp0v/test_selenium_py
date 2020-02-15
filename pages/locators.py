from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    USER_NAME = (By.NAME, "login-username")
    REG_EMAIL = (By.NAME, "registration-email")
