from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.automationtesting.in/Alerts.html")

"""
driver.find_element(By.ID,"username").send_keys("student")

driver.find_element(By.ID,"password").send_keys("Password123")

txt=driver.find_element(By.ID,"submit")

print(txt.text)

txt.click()

"""
driver.save_screenshot("before_alert.png")

driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()

alert=driver.switch_to.alert


print(alert.text)

alert.accept()




