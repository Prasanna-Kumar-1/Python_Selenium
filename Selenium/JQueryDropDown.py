from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()
time.sleep(2)


# Generic function to go through options of drop down and select a particular option
def select_values_from_dropdown(options_list, value):
    if not value[0] == 'All':
        for ele in drop_down_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in options_list:
                ele.click()
        except Exception as e:
            print(e)


# First Click on the Drop down
driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(3)

# Collect all the options of the drop down using driver.find_elements.
# this results in a list
drop_down_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
values_of_drop_down_list = ['choice 2', 'choice 3', 'choice 6 2 2']
values_of_drop_down_list = ['choice 2']
# values_of_drop_down_list = ['All']

# Calling the generic function.
# The arguments to this function are (1) drop_down_list & (2) List of values you wish to select
select_values_from_dropdown(drop_down_list, values_of_drop_down_list)
