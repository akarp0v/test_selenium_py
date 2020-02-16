from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_inp = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_inp.send_keys(email)
        pass1_inp = self.browser.find_element(*LoginPageLocators.PASS_INPUT_1)
        pass1_inp.send_keys(password)
        pass2_inp = self.browser.find_element(*LoginPageLocators.PASS_INPUT_2)
        pass2_inp.send_keys(password)
        submit_btn = self.browser.find_element(*LoginPageLocators.SUBMIT_BTN)
        submit_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверка на корректный url адрес
    def should_be_login_url(self):
        assert 'login' in self.url

    # проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.USER_NAME), \
            "Login field is not presented"

    # проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), \
            "Registration field is not presented"
