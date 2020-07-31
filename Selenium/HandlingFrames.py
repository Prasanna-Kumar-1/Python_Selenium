from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get('http://www.londonfreelance.org/courses/frames/index.html')

outer_frame_element = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(outer_frame_element)
header_value = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
print(header_value)

#Switching focus to the default frame
driver.switch_to.default_content()
time.sleep(3)

#Switching focus to the Parent frame
driver.switch_to.parent_frame()
time.sleep(3)

driver.quit()