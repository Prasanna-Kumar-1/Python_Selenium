# Basic approach of data driven approach by reading the data from excel source
# Need to import xlrd library to extract data from Excel spreadsheets (.xls and .xlsx)
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(2)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()

url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
second_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
mail_id = driver.find_element(By.ID, 'Form_submitForm_Email')
job_title = driver.find_element(By.ID, 'Form_submitForm_JobTitle')
company = driver.find_element(By.ID, 'Form_submitForm_CompanyName')
phone = driver.find_element(By.ID, 'Form_submitForm_Contact')

# Open Excel Work Book
workbook = xlrd.open_workbook("/Selenium/DataFile.xlsx")
# Open the Sheet
sheet = workbook.sheet_by_name("Login")

# 1. Get the total number of rows
rowCount = sheet.nrows
print(rowCount)

# 2. Get the total number of columns
colCount = sheet.ncols
print(colCount)

# Read through the excel sheet row by row and send the data
for current_row in range(1, rowCount):
    url_value = sheet.cell_value(current_row, 0)
    first_name_value = sheet.cell_value(current_row, 1)
    second_name_value = sheet.cell_value(current_row, 2)
    mail_id_value = sheet.cell_value(current_row, 3)
    job_title_value = sheet.cell_value(current_row, 4)
    company_value = sheet.cell_value(current_row, 5)
    phone_value = sheet.cell_value(current_row, 6)

    url.clear()
    url.send_keys(url_value)
    first_name.clear()
    first_name.send_keys(first_name_value)
    second_name.clear()
    second_name.send_keys(second_name_value)
    mail_id.clear()
    mail_id.send_keys(mail_id_value)
    job_title.clear()
    job_title.send_keys(job_title_value)
    company.clear()
    company.send_keys(company_value)
    phone.clear()
    phone.send_keys(phone_value)

# Close the driver Instance
driver.quit()