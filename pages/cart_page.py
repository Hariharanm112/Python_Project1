from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    Checkout=(By.XPATH,"//a[contains(text(),'Proceed')]")
    Place_order=(By.CSS_SELECTOR,"a[href*='payment']")



    def check_cart(self):
        self.click(self.Checkout)
        self.click(self.Place_order)