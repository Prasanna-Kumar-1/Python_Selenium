from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Yash\\PycharmProjects\\Drivers\\chromedriver.exe")
driver.get("http://www.google.com.au")
driver.implicitly_wait(3)

driver.find_element(By.NAME, 'q').send_keys("Sydney")
search_button = driver.find_element(By.XPATH, "//body[@id='gsr']/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div/div/div/center/input[1]")
search_button.click()

print(driver.title)

driver.quit()