# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 测试2.py
@Time    : 2025/7/9 15:43
@Author  : Echo Wang
'''



# 在定位时，有些元素含义特殊符合：. X   需要进行转移r''或用'\'进行转移


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
flag = 11
if flag == 1:
    ...

    driver.get('https://refactoringguru.cn/design-patterns/singleton')
    locator = 'xpath','//*[@class="type"][1]'
    ele1 = driver.find_element(*locator)
    print(driver.current_url)
    # print(driver.get_cookies())
    print(driver.session_id)
    print(ele1.id)
    print(ele1)

flag = 11
if flag == 1:
    ...
    driver.get('https://news.baidu.com/')
    locator = 'xpath', '//*[@id="s_btn_wr"]'
    ele1 = driver.find_element(*locator)
    print(ele1)
    print("-"*10)
    print(ele1.text)
    print("-" * 10)
    print(ele1.get_attribute("value"))



flag = 1
if flag == 1:
    ...
    driver.get('https://news.baidu.com/')
    locator = 'xpath', '//*[@class="hdline0"]//a'
    ele1 = driver.find_element(*locator)
    # print(ele1)
    # print("-" * 10)
    # print(ele1.text)
    # print("-" * 10)
    # print(ele1.get_attribute("value"))
    # print("-" * 10)
    driver.execute_script("arguments[0].setAttribute('data-custom', '123')", ele1)
    print(ele1.get_attribute("data-custom"))
    print("-" * 10)
    driver.execute_script("arguments[0].setAttribute('value', '我是测试的value')", ele1)
    print(ele1.get_attribute("value"))
    print("-" * 10)
    print(ele1.text)
