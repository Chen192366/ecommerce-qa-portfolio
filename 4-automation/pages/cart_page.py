from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    URL = "https://www.saucedemo.com/cart.html"

    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Remove')]")

    def is_loaded(self):
        return self.is_visible(self.TITLE)

    def get_cart_item_count(self):
        return self.get_element_count(self.CART_ITEMS)

    def remove_item(self, index=0):
        buttons = self.find_all(self.REMOVE_BUTTONS)
        if index < len(buttons):
            buttons[index].click()

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BTN)
