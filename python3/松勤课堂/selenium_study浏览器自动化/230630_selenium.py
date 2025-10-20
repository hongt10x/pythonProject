# coding: utf8
# test_selenium.py
# 2023/6/9

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# with WebDriver() as driver:
# with webdriver.Chrome() as driver:
#     # driver.get('http://www.baidu.com')
#
#     print('|对象或方法|说明|')
#     print('|---|---|')
#     for _ in dir(driver):
#         if _[0] != '_':
#             print('|', _, '||')


# with webdriver.Chrome() as driver:
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
ret =driver.find_element(By.TAG_NAME, 'p').text
print(ret)
ret =driver.find_element('tag name', 'p')
print(ret)

