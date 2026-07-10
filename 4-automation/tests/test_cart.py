from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:

    def setup_cart_with_one_item(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(0)

    def test_navigate_to_cart(self, driver):
        self.setup_cart_with_one_item(driver)
        inventory = InventoryPage(driver)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.is_loaded()
        assert cart.get_cart_item_count() == 1

    def test_remove_item_from_cart(self, driver):
        self.setup_cart_with_one_item(driver)
        inventory = InventoryPage(driver)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.get_cart_item_count() == 1
        cart.remove_item(0)
        assert cart.get_cart_item_count() == 0

    def test_continue_shopping_redirects_to_inventory(self, driver):
        self.setup_cart_with_one_item(driver)
        inventory = InventoryPage(driver)
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.continue_shopping()

        assert InventoryPage(driver).is_loaded()

    def test_checkout_button_redirects(self, driver):
        self.setup_cart_with_one_item(driver)
        inventory = InventoryPage(driver)
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.go_to_checkout()

        assert "checkout-step-one" in driver.current_url
