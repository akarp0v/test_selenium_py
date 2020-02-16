from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def cart_should_have_empty_message(self):
        assert self.browser.find_element(*CartPageLocators.EMPTY_MESSAGE), \
            "Text 'Your basket is empty' was found"

    def cart_should_be_empty(self):
        assert self.is_not_element_present(*CartPageLocators.GOODS_LINK), \
            "Cart is not empty, but should be"

    def cart_should_not_be_empty(self):
        assert self.is_element_present(*CartPageLocators.GOODS_LINK), \
            "Cart is empty, but should not be"
