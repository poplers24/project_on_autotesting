from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def adding_a_product_to_basket(self):
        button_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_TO_BASKET)
        button_to_basket.click()

    def item_added_to_basket(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        message_product_title = self.browser.find_element(*ProductPageLocators.MESSAGE_TITLE_PRODUCT).text
        assert product_title in message_product_title, "The product name in the cart does not match the product added"

    def compare_the_price_of_the_product_in_sum_basket(self):
        price_to_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        sum_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_PRODUCT).text
        assert price_to_product in sum_basket, "The cart amount does not match the price of the product"


