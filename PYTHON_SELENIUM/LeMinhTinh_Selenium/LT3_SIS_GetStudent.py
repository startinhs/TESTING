import csv
import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://sis.ou.edu.vn/')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, 'button.login100-form-btn').click()
Select(driver.find_element(By.ID, 'form-usertype')).select_by_index(0)
with open('OuAcc.csv','r',newline='',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        user = r['user']
        password = r['password']

driver.find_element(By.ID, 'form-username').send_keys(user)
driver.find_element(By.ID, 'form-password').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'button.m-loginbox-submit-btn').click()
# driver.find_element(By.CSS_SELECTOR, 'button.btn-success').click()
driver.implicitly_wait(10)

GPA = driver.find_element(By.XPATH, '//*[@id="dtbhk"]/table/tbody/tr[7]/td[4]').text
DRL = driver.find_element(By.ID, 'DiemRLTK').text
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul[2]/li/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//a[@href="https://sis.ou.edu.vn/tienich/svinfo"]').click()
info = driver.find_elements(By.CSS_SELECTOR, 'div> div > ul > li > b')
for i in info:
    print(i.text)
print(GPA)
print(DRL)
driver.close()