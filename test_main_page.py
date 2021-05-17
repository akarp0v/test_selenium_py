from app import MainPage, LoginPage, CartPage, Const
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # Открываем главную страницу
    # Переходим на страницу логина
    def test_guest_can_go_to_login_page(self, browser):
        link = Const.MAIN_URL
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # Открываем главную страницу
    # Проверяем, что есть логин
    def test_guest_should_see_login_link(self, browser):
        link = Const.MAIN_URL
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


# Открываем главную страницу
# Переходим в корзину по кнопке в шапке сайта
# Проверяем, что в корзине нет товаров
# Проверяем, что есть текст на английском о том, что корзина пуста
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = Const.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()
    cart_page.cart_should_have_empty_message()
