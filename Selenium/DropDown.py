from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("https://www.spicejet.com/")
driver.maximize_window()

# Create a generic select method to handle element and values
# It takes 2 arguments. (1) Actual Element  (2) Value by which you will select


def select_values(element, value):
    select = Select(element)
    select.select_by_value(value)


currency_dropdown = driver.find_element(By.ID, "ctl00_mainContent_DropDownListCurrency")
select = Select(currency_dropdown)

select_values(currency_dropdown, 'AED')

# Selecting by Visible Text
select.select_by_visible_text('AED')

# Selecting by Index
select.select_by_index(3)

# Select by Value
select.select_by_value('USD')

print(select.is_multiple)

# All the options present in the drop down list
currency_list = select.options

for ele in currency_list:
    if ele.text == "Select":
        print("This is actually is not an option")
    else:
        print(ele.text)

# Implementation of driver.find_elements
currency_list = driver.find_elements(By.ID, "ctl00_mainContent_DropDownListCurrency")
print(currency_list)

for ele in currency_list:
    print(ele.text)
