from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MAIN_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    MAIN_BOOK_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE_MSG = (By.CSS_SELECTOR, ".alert-info strong")
    BOOK_NAME_MSG = (By.CSS_SELECTOR, ".alert-success strong")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success")
