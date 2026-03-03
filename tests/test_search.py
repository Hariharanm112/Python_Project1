from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.product_page import Products
import pytest
import time
@pytest.mark.order(2)

def test_product_add(driver):
    home=HomePage(driver)
    home.load()
    print("Finding Products link...")
    home.go_to_products()


    print("clickrf thr product")
    product=Products(driver)
    print("dint went")
    product.product_add_cart("blue top")
    print("all is well")

