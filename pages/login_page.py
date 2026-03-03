from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Login_page(BasePage):
    URL = "https://automationexercise.com/"

    Mai_id = (By.XPATH, "//input[@placeholder='Email Address']")
    Password = (By.XPATH, "//input[@placeholder='Password']")
    Submit=(By.XPATH, "//button[contains(text(),'Login')]")

    def login_browser(self,username,password):
        self.enter_text(self.Mai_id,username)
        self.enter_text(self.Password,password)
        self.click(self.Submit)

