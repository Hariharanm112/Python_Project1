
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import logging

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)   # ✅ Proper way

    from selenium.common.exceptions import ElementClickInterceptedException

    def click(self, locator, scroll=True):
        try:
            self.logger.info(f"Clicking element: {locator}")

            element = self.wait.until(EC.presence_of_element_located(locator))

            if scroll:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", element
                )

            self.wait.until(EC.element_to_be_clickable(locator)).click()
            self.logger.info("Click successful")

        except ElementClickInterceptedException:
            self.logger.warning("Click intercepted, using JS click")
            self.driver.execute_script("arguments[0].click();", element)

        except TimeoutException:
            self.logger.error(f"Element not clickable: {locator}")
            self.driver.save_screenshot("click_error.png")
            raise

    def enter_text(self, locator, text):
        self.logger.info(f"Entering text '{text}' into {locator}")

        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    def switch_element(self,locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))


