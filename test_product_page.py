from app import ProductPage, LoginPage, CartPage, Const
from essential_generators import DocumentGenerator as Gen
import pytest


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f'{Const.MAIN_URL}{Const.LOGIN}'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(Gen().email(), '111qQ22Ww')
        page.should_be_authorized_user()

    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    def test_user_cant_see_success_message(self, browser):
        link = f'{Const.MAIN_URL}{Const.CATALOG_207}'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    # Открываем страницу товара
    # Проверяем, есть ли кнопка "Добавить в корзину"
    # Проверяем, есть ли основная информация о товаре
    # Добавляем в корзину
    # Получаем код
    # Проверяем название товара
    # Проверяем цену товара
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f'{Const.MAIN_URL}{Const.CATALOG_207}?promo=newYear2019'
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
        page.open()
        page.should_be_cart_link()
        page.should_be_product_info()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.check_chosen_product_name()
        page.check_chosen_product_price()


# Открываем страницу товара
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
def test_guest_cant_see_success_message(browser):
    link = f'{Const.MAIN_URL}{Const.CATALOG_207}'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


# Открываем страницу товара
# Проверяем, есть ли кнопка "Добавить в корзину"
# Проверяем, есть ли основная информация о товаре
# Добавляем в корзину
# Получаем код
# Проверяем название товара
# Проверяем цену товара
@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    f"{Const.MAIN_URL}{Const.CATALOG_207}/?promo=offer{n}" if n != 7
    else pytest.param(f"{Const.MAIN_URL}{Const.CATALOG_207}/?promo=offer{n}", marks=pytest.mark.xfail)
    for n in range(10)
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.should_be_product_info()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_chosen_product_name()
    page.check_chosen_product_price()


# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.xfail(reason="fixing this bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"{Const.MAIN_URL}{Const.CATALOG_207}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_disappeared
@pytest.mark.xfail(reason="fixing this bug")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"{Const.MAIN_URL}{Const.CATALOG_207}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappeared()


# Открываем страницу товара
# Проверяем, что есть логин
def test_guest_should_see_login_link_on_product_page(browser):
    link = f"{Const.MAIN_URL}{Const.CATALOG_95}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# Открываем страницу товара
# Переходим в корзину по кнопке в шапке сайта
# Проверяем, что в корзине нет товаров
# Проверяем, что есть текст на английском о том, что корзина пуста
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = f"{Const.MAIN_URL}{Const.CATALOG_95}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()
    cart_page.cart_should_have_empty_message()


# Открываем страницу товара
# Проверяем, что есть логин
# Переходим на страницу логина
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = f"{Const.MAIN_URL}{Const.CATALOG_95}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
