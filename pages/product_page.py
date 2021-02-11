from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def prices_should_be_equal(self):
        book_price = self.browser.find_element(*ProductPageLocators.MAIN_PRICE).text
        basket_total_msg = self.browser.find_element(*ProductPageLocators.PRICE_MSG).text
        assert book_price == basket_total_msg

    def book_names_should_be_equal(self):
        book_name = self.browser.find_element(*ProductPageLocators.MAIN_BOOK_NAME).text
        book_name_msg = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MSG).text
        assert book_name == book_name_msg
