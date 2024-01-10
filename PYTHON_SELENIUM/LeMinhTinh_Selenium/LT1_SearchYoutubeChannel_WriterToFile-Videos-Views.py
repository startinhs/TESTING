import csv
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
# channel = input('Enter channel: ')
channel = 'startinhs'
driver.implicitly_wait(5)
searchBox = driver.find_element(By.NAME, 'search_query')

searchBox.send_keys(channel)
searchBox.submit()
driver.find_element(By.ID, 'main-link').click()

###Chuyen tab videos
#cach1
# driver.find_element(By.CSS_SELECTOR, '#tabsContent > yt-tab-group-shape > div.yt-tab-group-shape-wiz__tabs > yt-tab-shape:nth-child(2) > div.yt-tab-shape-wiz__tab').click()

#cach2
# tab = driver.find_elements(By.CSS_SELECTOR, 'div.yt-tab-shape-wiz__tab')
# for t in tab:
#     if t.text == 'Videos':
#         t.click()
#         break

#cach3
driver.find_element(By.LINK_TEXT, 'Videos').click()

driver.implicitly_wait(10)
videos = driver.find_elements(By.CSS_SELECTOR, '#content > ytd-rich-grid-media')

# listVideo = []
# for v in videos:
#     try:
#         videoName = v.find_element(By.CSS_SELECTOR, '#meta a').text
#         view = v.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(3)').text
#         listVideo.append({'videoName': videoName, 'view': view})
#     except NoSuchElementException:
#         print("Loi!")
# print(listVideo)
# with open('startinhs.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=['videoName', 'view'])
#     writer.writeheader()
#     for row in listVideo:
#         writer.writerow(row)
#     print("Ghi file thanh cong!")


with open('startinhs.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['videoName', 'view', 'link'])
    writer.writeheader()
    for v in videos:
        try:
            videoName = v.find_element(By.CSS_SELECTOR, '#meta a').text
            view = v.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(3)').text
            link = v.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            writer.writerow({'videoName': videoName, 'view': view, 'link': link})
        except NoSuchElementException:
            print("Loi!")
    print("Ghi file thanh cong!")

driver.implicitly_wait(10)
time.sleep(10)
driver.close()