from .base_page import BasePage
from .locators import SearchPageLocators

class SearchPage(BasePage):
    def search_the_result_on_the_search_page(self, desired):
        self.should_be_in_breadcrumbs_search_value(desired)
        self.should_be_search_value_in_page_title(desired)
        self.should_be_found_result()
        self.should_be_found_result_match_the_desired_one(desired)
        self.should_be_search_url()

    def should_be_in_breadcrumbs_search_value(self, desired):
        breadcrumb = self.browser.find_element(*SearchPageLocators.BREADCRUMB).text
        assert desired in breadcrumb, "The value you are looking for is missing in the breadcrumbs"

    def should_be_search_value_in_page_title(self, desired):
        h1_search_page = self.browser.find_element(*SearchPageLocators.H1_SEARCH_PAGE).text
        assert desired in h1_search_page, "The value you are looking for is not inthe page title"

    def should_be_found_result(self):
        found_result = self.browser.find_element(*SearchPageLocators.NUMBER_FOUND_RESULT).text
        assert found_result == "1", "The result found does not match the expected"

    def should_be_found_result_match_the_desired_one(self, desired):
        search_result = self.browser.find_element(*SearchPageLocators.PRODUCT_NAME_IN_SEARCH_RESULT).text
        assert desired == search_result, "Product found does not match what you are looking for"

    def should_be_search_url(self):
        search_url = self.browser.current_url
        assert "/search/" in search_url, "Search page url does not match expected"