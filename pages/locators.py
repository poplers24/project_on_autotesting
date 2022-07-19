from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
    LANGUAGE_SELECTION = (By.CSS_SELECTOR, "[name='language']")
    BUTTON_LANG_SWITCH = (By.CSS_SELECTOR, "#language_selector button.btn.btn-default")
    FIELD_SEARCH = (By.CSS_SELECTOR, "#id_q")
    BUTTON_SEARCH = (By.CSS_SELECTOR, ".navbar-form.navbar-right > .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert:nth-child(1) > div strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert-info > .alertinner p strong")

class BasketPageLocators():
    ITEMS_TO_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6")
    PRODUCT_LIST_TO_BASKET = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")

class SearchPageLocators():
    BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb > .active")
    H1_SEARCH_PAGE = (By.CSS_SELECTOR, ".page-header > h1")
    NUMBER_FOUND_RESULT = (By.CSS_SELECTOR, ".form-horizontal > strong")
    PRODUCT_NAME_IN_SEARCH_RESULT = (By.CSS_SELECTOR, "h3")
