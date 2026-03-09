from pages.home_page import HomePage
from pages.product_page import Products
import pytest
from utils.logger import setup_logger

logger = setup_logger()
@pytest.mark.order(2)
def test_product_add(driver, search_data):

    logger.info("Starting test_product_add")

    home = HomePage(driver)
    logger.info("Loading home page")
    home.load()

    logger.info("Navigating to products page")
    home.go_to_products()

    product_page = Products(driver)

    for product in search_data:
        logger.info(f"Adding product to cart: {product['name']}")
        product_page.product_add_cart(product["name"])

    logger.info("Completed test_product_add")
