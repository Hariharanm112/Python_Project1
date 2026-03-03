import time
import pytest
from pages.login_page import Login_page
from pages.home_page import HomePage

@pytest.mark.order(1)

def test_login(driver):
    home=HomePage(driver)
    home.load()
    home.go_to_login()

    login=Login_page(driver)
    login.login_browser("mhariharan165@gmail.com","8825911487@Hari")


