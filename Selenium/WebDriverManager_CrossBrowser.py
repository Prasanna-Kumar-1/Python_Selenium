from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.common.by import By

browserName = "ie"

if browserName == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "ie":
    driver = webdriver.Ie(IEDriverManager().install())
else:
    print("Incorrect Browser Name")
    raise Exception('driver is not found')

driver.implicitly_wait(3)
driver.get("https://google.com")
search_box = driver.find_element(By.XPATH, "//input[@name='q']")
search_box.send_keys("Prasanna")

driver.quit()