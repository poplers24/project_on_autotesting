from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

def test_guest_can_add_product_bo_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.adding_a_product_to_basket()
    page.solve_quiz_and_get_code()
    page.item_added_to_basket()
    page.compare_the_price_of_the_product_in_sum_basket()




