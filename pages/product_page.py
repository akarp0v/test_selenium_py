from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def add_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        cart_link.click()

    def should_be_cart_link(self):
        assert self.is_element_present(*ProductPageLocators.CART_LINK), \
               "Cart link is not presented"

    def should_be_product_info(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_INFO), \
               "Main product info is not presented"

    def check_chosen_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text, \
               'Different Product NAMES'

    def check_chosen_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text, \
               'Different Product PRICES'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
