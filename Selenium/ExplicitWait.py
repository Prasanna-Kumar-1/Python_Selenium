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

# Wait until presence of element is located
mail_id = wait.until(expcond.presence_of_element_located((By.ID, 'username')))
mail_id.send_keys('test@gmail.com')

# wait.until(expcond.title_is('HubSpot Login'))
wait.until(expcond.title_contains('Hub'))
print(driver.title)

driver.quit()

