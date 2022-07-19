from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def go_to_basket_page(self):
        button_to_basket = self.browser.find_element(*BasePageLocators.BUTTON_TO_BASKET)
        button_to_basket.click()

    def should_be_language_switcher(self):
        assert self.is_element_present(*BasePageLocators.LANGUAGE_SELECTION), "Language switcher is not presented"

    def choose_a_language(self, lang):
        language_selection = Select(self.browser.find_element(*BasePageLocators.LANGUAGE_SELECTION))
        language_selection.select_by_value(lang)

    def switch_language(self):
        button_lang_switch = self.browser.find_element(*BasePageLocators.BUTTON_LANG_SWITCH)
        button_lang_switch.click()

    def should_be_language_in_url(self, lang):
        language_url = self.browser.current_url
        assert lang in language_url, "Page url does not match the selected language"

    def entering_a_value_in_the_search_field(self, value):
        input_search = self.browser.find_element(*BasePageLocators.FIELD_SEARCH)
        input_search.send_keys(value)

    def start_search_by_button(self):
        button_search = self.browser.find_element(*BasePageLocators.BUTTON_SEARCH)
        button_search.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

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

    # метод проверки, что элемент не появляется на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # метод проверки, что элемент исчезает
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True





