from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    URL = "https://www.saucedemo.com/inventory.html"

    TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def is_loaded(self):
        return self.is_visible(self.TITLE)

    def get_product_count(self):
        return self.get_element_count(self.PRODUCT_ITEMS)

    def add_product_to_cart(self, index=0):
        items = self.find_all(self.PRODUCT_ITEMS)
        add_button = items[index].find_element(By.XPATH, ".//button[contains(text(), 'Add to cart')]")
        add_button.click()

    def remove_product_from_cart(self, index=0):
        items = self.find_all(self.PRODUCT_ITEMS)
        remove_button = items[index].find_element(By.XPATH, ".//button[contains(text(), 'Remove')]")
        remove_button.click()

    def sort_by(self, option_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_value(option_value)

    def get_cart_count(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except Exception:
            return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)

    def get_all_prices(self):
        elements = self.find_all(self.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]

    def get_all_names(self):
        elements = self.find_all(self.PRODUCT_NAMES)
        return [el.text for el in elements]
