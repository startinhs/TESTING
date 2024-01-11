import csv
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://vnexpress.net/')
driver.find_element(By.CSS_SELECTOR, '#dark_theme > header > div > a').click()
driver.find_element(By.LINK_TEXT, 'Khoa học').click()
posts = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
ListPost = []
for row in posts:
    try:
        title = row.find_element(By.TAG_NAME, 'a').get_attribute('title') #h3>a
        content = row.find_element(By.CSS_SELECTOR, 'p > a').text
        link = row.find_element(By.CSS_SELECTOR, 'h3 > a').get_attribute('href')
        # print("----",title,"----")
        # print(content)
        # print(link)
        # print("*******************************************")

    except NoSuchElementException:
        pass
    ListPost.append({'Title': title, 'Decription': content, 'Link': link})
print("Da trich xuat thanh cong!")

driver.save_screenshot('LeMinhTinh.png')

with open('LeMinhTinh.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Title', 'Decription', 'Link'])
    writer.writeheader()
    for row in ListPost:
        # title = row.find_element(By.TAG_NAME, 'a').get_attribute('title')
        # content = row.find_element(By.CSS_SELECTOR, 'p > a').text
        # link = row.find_element(By.CSS_SELECTOR, 'h3 > a').get_attribute('href')
        writer.writerow(row)
    print("Da ghi xong file!")

driver.close()
