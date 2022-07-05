from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.should_not_be_product_in_basket()
        self.should_be_text_that_the_basket_empty()

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BASKET), "Item in the cart is present"

    def should_be_text_that_the_basket_empty(self):
        basket_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).text
        assert "Your basket is empty." in basket_empty_text, "The text that the basket is empty is missing"