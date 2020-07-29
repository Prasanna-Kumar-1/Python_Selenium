from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

right_click_element = driver.find_element(By.XPATH, "//span[contains(text(),'right click me')]")
act_chain = ActionChains(driver)
act_chain.context_click(right_click_element).perform()

right_click_elements = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')
for ele in right_click_elements:
    print(ele.text)
    if ele.text == 'Copy':
        ele.click()
        break