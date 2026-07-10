from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckoutE2E:

    def test_complete_purchase_flow(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(0)
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.go_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("Zhang", "San", "100000")
        checkout.click_continue()

        assert "checkout-step-two" in driver.current_url

        checkout.click_finish()

        assert "checkout-complete" in driver.current_url
        assert "Thank you for your order!" in checkout.get_complete_message()

        checkout.back_home()
        assert InventoryPage(driver).is_loaded()

    def test_checkout_empty_first_name_shows_error(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(0)
        inventory.go_to_cart()
        CartPage(driver).go_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("", "San", "100000")
        checkout.click_continue()

        assert "First Name is required" in checkout.get_error_message()

    def test_checkout_empty_last_name_shows_error(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(0)
        inventory.go_to_cart()
        CartPage(driver).go_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("Zhang", "", "100000")
        checkout.click_continue()

        assert "Last Name is required" in checkout.get_error_message()

    def test_checkout_empty_postal_code_shows_error(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(0)
        inventory.go_to_cart()
        CartPage(driver).go_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("Zhang", "San", "")
        checkout.click_continue()

        assert "Postal Code is required" in checkout.get_error_message()

    def test_cancel_checkout_returns_to_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(0)
        inventory.go_to_cart()
        CartPage(driver).go_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.cancel()

        assert CartPage(driver).is_loaded()

    def test_logout_after_purchase(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.logout()

        assert login_page.is_on_login_page()
