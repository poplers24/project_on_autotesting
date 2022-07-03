from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def adding_a_product_to_basket(self):
        button_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_TO_BASKET)
        button_to_basket.click()

    def should_be_item_added_to_basket(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        message_product_title = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_title == message_product_title, "The product name in the cart does not match the product added"

    def should_be_compare_the_price_of_the_product_in_sum_basket(self):
        price_to_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        sum_basket = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert price_to_product == sum_basket, "The cart amount does not match the price of the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_the_message_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The message didn't disappear"


