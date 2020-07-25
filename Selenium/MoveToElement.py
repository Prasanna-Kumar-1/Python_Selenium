from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://www.spicejet.com/")
driver.fullscreen_window()
time.sleep(5)

# ActionsChains() method implementation
act_chains = ActionChains(driver)

login_element = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
act_chains.move_to_element(login_element).perform()

spice_club_members_element = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
act_chains.move_to_element(spice_club_members_element).perform()

member_login_element = driver.find_element(By.LINK_TEXT, 'Member Login')
member_login_element.click()

time.sleep(3)
driver.quit()