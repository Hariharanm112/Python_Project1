from selenium import     webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    from selenium.common.exceptions import ElementClickInterceptedException

    def click(self, locator, scroll=True):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))

            if scroll:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", element
                )

            self.wait.until(EC.element_to_be_clickable(locator)).click()

        except ElementClickInterceptedException:
            print("Click intercepted, using JS click")
            self.driver.execute_script("arguments[0].click();", element)

        except TimeoutException:
            print(f"Element not clickable: {locator}")
            self.driver.save_screenshot("click_error.png")
            raise
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    def switch_element(self,locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))


