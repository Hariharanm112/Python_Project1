from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://automationexercise.com/products"

    LOGIN_LINK = (By.LINK_TEXT, "Signup / Login")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[href='/products']")
    CART_LINK = (By.LINK_TEXT, "Cart")

    def load(self):
        self.driver.get(self.URL)

    def go_to_login(self):
        self.click(self.LOGIN_LINK)


    def go_to_products(self):
        print("Finding Products link...")

        self.click(self.PRODUCTS_LINK)
        print("Clicked Products link")
    def go_to_cart(self):
        self.click(self.CART_LINK)