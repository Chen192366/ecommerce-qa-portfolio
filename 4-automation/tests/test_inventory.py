from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    def login_and_goto_inventory(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        return InventoryPage(driver)

    def test_product_count_is_six(self, driver):
        inventory = self.login_and_goto_inventory(driver)
        assert inventory.get_product_count() == 6

    def test_sort_price_low_to_high(self, driver):
        inventory = self.login_and_goto_inventory(driver)
        inventory.sort_by("lohi")

        prices = inventory.get_all_prices()
        assert prices == sorted(prices)

    def test_sort_price_high_to_low(self, driver):
        inventory = self.login_and_goto_inventory(driver)
        inventory.sort_by("hilo")

        prices = inventory.get_all_prices()
        assert prices == sorted(prices, reverse=True)

    def test_sort_name_a_to_z(self, driver):
        inventory = self.login_and_goto_inventory(driver)
        inventory.sort_by("az")

        names = inventory.get_all_names()
        assert names == sorted(names)

    def test_sort_name_z_to_a(self, driver):
        inventory = self.login_and_goto_inventory(driver)
        inventory.sort_by("za")

        names = inventory.get_all_names()
        assert names == sorted(names, reverse=True)

    def test_add_single_product_to_cart(self, driver):
        inventory = self.login_and_goto_inventory(driver)
        inventory.add_product_to_cart(0)

        assert inventory.get_cart_count() == 1

    def test_add_multiple_products_to_cart(self, driver):
        inventory = self.login_and_goto_inventory(driver)
        inventory.add_product_to_cart(0)
        inventory.add_product_to_cart(1)
        inventory.add_product_to_cart(2)

        assert inventory.get_cart_count() == 3

    def test_add_and_remove_product_from_cart(self, driver):
        inventory = self.login_and_goto_inventory(driver)
        inventory.add_product_to_cart(0)
        assert inventory.get_cart_count() == 1

        inventory.remove_product_from_cart(0)
        assert inventory.get_cart_count() == 0
