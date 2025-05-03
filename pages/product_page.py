from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

    def add_to_basket(self):
        btn = self.browser.find_element(*self.ADD_TO_BASKET)
        btn.click()

    def should_be_success_message(self):
        product_name = self.browser.find_element(*self.PRODUCT_NAME).text
        success_name = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert product_name == success_name, "Product name does not match in success message"

    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*self.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert product_price == basket_total, "Basket total does not match product price"
