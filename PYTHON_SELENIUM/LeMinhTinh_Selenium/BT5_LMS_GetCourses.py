from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://lms.ou.edu.vn/')
driver.find_element(By.CSS_SELECTOR,'a.main-btn').click()
driver.find_element(By.CSS_SELECTOR,'button.login100-form-btn').click()
userType = Select(driver.find_element(By.ID,'form-usertype'))
userType.select_by_index(0)
with open('test.csv','r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        u = row['user']
        p = row['password']
(driver.find_element(By.NAME,'form-username')).send_keys(u)
(driver.find_element(By.NAME,'form-password')).send_keys(p)
driver.find_element(By.CLASS_NAME,'m-loginbox-submit-btn').click()
driver.implicitly_wait(10)
# course = driver.find_elements(By.CSS_SELECTOR,'.dashboard-card .course-info-container .align-items-start a')
course = driver.find_elements(By.CSS_SELECTOR,'.course-info-container > div > div > a')
for c in course:
    print(c.text)
driver.close()