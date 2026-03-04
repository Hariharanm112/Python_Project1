import time
import pytest

from pages.login_page import Login_page
from pages.home_page import HomePage


@pytest.mark.order(1)
def test_login(driver, login_data):   # login_data is a fixture returning list of users
    for user in login_data:
        home = HomePage(driver)
        home.load()
        home.go_to_login()

        login = Login_page(driver)
        login.login_browser(user["username"], user["password"])

