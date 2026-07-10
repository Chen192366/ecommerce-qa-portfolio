import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:

    def test_login_with_valid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded()
        assert "inventory" in driver.current_url

    def test_login_with_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "wrong_password")

        assert login_page.is_error_displayed()
        assert "Username and password do not match" in login_page.get_error_message()
        assert login_page.is_on_login_page()

    def test_login_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        assert login_page.is_error_displayed()
        assert "Sorry, this user has been locked out" in login_page.get_error_message()

    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("", "", "Username is required"),
    ])
    def test_login_empty_fields(self, driver, username, password, expected_error):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)

        assert login_page.is_error_displayed()
        assert expected_error in login_page.get_error_message()
