import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage

@pytest.mark.order(3)
def test_cart(driver):
    cart=HomePage(driver)
    cart.load()
    cart.go_to_cart()
    add_cart=CartPage(driver)
    add_cart.check_cart()
