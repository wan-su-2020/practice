from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time

url = 'https://www.musinsa.com/categories/item/001'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

title_list=[]
shorts_list=[]
items = soup.find('ul', id='searchList').find_all('li', class_='li_box')
for i, item in enumerate(items):
    title = item.find('div', class_='article_info').find('p', class_='list_info').find('a').get_text(strip=True)
    image_url = 'https:' + item.find('img', class_='lazyload')['data-original']
    title_list.append(title)

    if '/' in title:
        title = title.replace('/', '-')
