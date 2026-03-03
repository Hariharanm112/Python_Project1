import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class Products(BasePage):
    Search=(By.ID,"search_product")
    submit_search=(By.ID,"submit_search")
    add_to_cart=(By.XPATH,"//div[@class='productinfo text-center']//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart']")
    Continue_shopping=(By.XPATH,"//button[contains(text(),'Continue Shopping')]")
    Body=(By.TAG_NAME, "body")



    def product_add_cart(self,product):
        self.click(self.Body,scroll=False)

        self.enter_text(self.Search,product)
        self.click(self.submit_search)
        # Scroll element into view (center)
        self.click(self.add_to_cart)
        self.click(self.Continue_shopping)

