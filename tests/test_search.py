from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.product_page import Products
import pytest
import time
@pytest.mark.order(2)
def test_product_add(driver, search_data):
    home = HomePage(driver)
    home.load()
    home.go_to_products()

    product_page = Products(driver)

    for product in search_data:   # iterate through all products
        product_page.product_add_cart(product["name"])
