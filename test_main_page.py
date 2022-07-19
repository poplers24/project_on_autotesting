from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
class TestLoginFormMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метотод страницы - переходим  на страницу логина
        # login_page = page.go_to_login_page() # явно возвращаем страницу — тип страницы ассоциирован с методом
        # login_page.should_be_login_page()
        login_page = LoginPage(browser, browser.current_url) # переход происходит неявно, страницу инициализируем в теле теста
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

# languages = {
#     "ar": "سلة التسوق فارغة",
#     "ca": "La seva cistella està buida.",
#     "cs": "Váš košík je prázdný.",
#     "da": "Din indkøbskurv er tom.",
#     "de": "Ihr Warenkorb ist leer.",
#     "en-gb": "Your basket is empty.",
#     "el": "Το καλάθι σας είναι άδειο.",
#     "es": "Tu carrito esta vacío.",
#     "fi": "Korisi on tyhjä",
#     "fr": "Votre panier est vide.",
#     "it": "Il tuo carrello è vuoto.",
#     "ko": "장바구니가 비었습니다.",
#     "nl": "Je winkelmand is leeg",
#     "pl": "Twój koszyk jest pusty.",
#     "pt": "O carrinho está vazio.",
#     "pt-br": "Sua cesta está vazia.",
#     "ro": "Cosul tau este gol.",
#     "ru": "Ваша корзина пуста",
#     "sk": "Váš košík je prázdny",
#     "uk": "Ваш кошик пустий.",
#     "zh-hans": "Your basket is empty.",
# }
# lang = [k for k in languages.keys()]
@pytest.mark.parametrize('langs', ["ar",  "ca", "cs", "da", "de", "en-gb",
                                   "el", "es", "fi", "fr", "it", "ko", "nl",
                                   "pl", "pt", "pt-br", "ro", "ru", "sk", "uk",
                                   pytest.param('zh-hans', marks=pytest.mark.xfail)])
def test_guest_switches_interface_language(browser, langs):
# def test_guest_switches_interface_language(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.choose_a_language(langs)
    page.switch_language()
    page.should_be_language_in_url(langs)

def test_guest_should_see_the_language_switcher(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_language_switcher()





