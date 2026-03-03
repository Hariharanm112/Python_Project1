import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.hookimpl(hookwrapper=True)
def Pytest_runtest_makereport(item,call):
        outcome=yield
        report=outcome.get_result()
        if report.when=="call"and report.failed:
                driver=item.funcargs.get("driver")
                if driver:
                        driver.save_screeshot(f"screenshot/{item.name}.png")
@pytest.fixture(scope='session')
def driver():
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
        options=options   # 🔥 THIS WAS MISSING
    )

    # Remove webdriver flag
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    yield driver
    driver.quit()
