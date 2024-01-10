from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

webdriver = webdriver.Chrome()
webdriver.get("https://www.facebook.com/?locale=vi_VN")
webdriver.implicitly_wait(10)
webdriver.find_element(By.XPATH,"//*[text()='Tạo tài khoản mới']").click()
webdriver.find_element(By.NAME,"lastname").send_keys("Le")
webdriver.find_element(By.NAME,"firstname").send_keys("Tinh")
webdriver.find_element(By.NAME,"reg_email__").send_keys("lmt181@gmail.com")
webdriver.find_element(By.NAME,"reg_email_confirmation__").send_keys("lmt181@gmail.com")
webdriver.find_element(By.NAME,"reg_passwd__").send_keys("12345")
Select(webdriver.find_element(By.NAME,"birthday_day")).select_by_visible_text("18")
Select(webdriver.find_element(By.NAME,"birthday_month")).select_by_visible_text("Tháng 1")
Select(webdriver.find_element(By.NAME,"birthday_year")).select_by_visible_text("2003")
webdriver.find_element(By.XPATH,"//label[text()='Nam']").click()
webdriver.find_element(By.NAME,"websubmit").click()
webdriver.close()
