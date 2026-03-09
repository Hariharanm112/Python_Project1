import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from selenium.webdriver.firefox.options import Options



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    print("HOOK EXECUTED:", report.when, report.failed)

    if report.when == "call" and report.failed:
        print("TEST FAILED")
        print("FUNCARGS:", item.funcargs)

        driver = item.funcargs.get("driver")
        print("DRIVER:", driver)

        if driver:
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(f"screenshots/{item.name}.png")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='session')
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()

        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Prevent automation detection (important)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)

    else:
        raise Exception("Browser not supported")
    yield driver
    driver.quit()


@pytest.fixture
def login_data():
    with open("test_data/login_data.json") as f:
        data = json.load(f)
    return data["users"]

@pytest.fixture
def search_data():
    with open("test_data/search_data.json")as f:
          data=json.load(f)
    return data["products"]


