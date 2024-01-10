from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://vnexpress.net/')
results = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
driver.implicitly_wait(15)
for re in results:
    try:
        text = re.find_element(By.TAG_NAME, 'h3').text
        print(text)
        print("*******************************************")
    except NoSuchElementException:
        print("Loi!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
driver.close()
