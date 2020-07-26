from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.fullscreen_window()
time.sleep(5)

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

act_chain = ActionChains(driver)
# act_chain.drag_and_drop(source, target).perform()

# Another way of dragging and dropping
# Chainable actions (1) Click and hold source element (2) Move to the Target Element (3) Release

act_chain.click_and_hold(source).move_to_element(target).release().perform()

time.sleep(3)
driver.quit()
