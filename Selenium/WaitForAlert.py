from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcond
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

# Specify maximum amount of time to wait for a specific condition
wait = WebDriverWait(driver, 10)

driver.find_element(By.NAME, 'proceed').click()
alert = wait.until(expcond.alert_is_present())
print(alert.text)
alert.accept()
driver.close()