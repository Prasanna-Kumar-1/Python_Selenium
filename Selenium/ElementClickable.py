from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcond
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/login")

# Specify maximum amount of time to wait for a specific condition
wait = WebDriverWait(driver, 10)

# Check whether a link is clickable
signup_link= wait.until(expcond.element_to_be_clickable((By.LINK_TEXT, 'Sign up')))
print(signup_link.text)

# Click the link
signup_link.click()

driver.close()
