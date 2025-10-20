# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：07_selenium元素定位.py
@Date    ：2024/4/16 15:28 
'''
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

flag = 11
if flag == 1:
    ...

    url = 'https://zhuanlan.zhihu.com/p/64947289'

    driver.get(url)
    # time.sleep(3)
    locator = 'css selector','.Zi.Zi--Close.Modal-closeIcon'
    WW(driver, 5, 0.5).until(EC.visibility_of_element_located(locator)).click()
    # WW(driver, 5, 0.5).until(EC.presence_of_element_located(locator)).click()
    # web_element = driver.find_element(*locator)
    # print(web_element)
    # web_element.click()
    time.sleep(1)
    # locator = ('css selector', '.language-python spapon')
    # web_elements = driver.find_elements(*locator)
    # print(web_elements)
    # for ele in web_elements:
    #     print(ele.text)
    locator = ('tag name', 'html')
    element = driver.find_element(*locator)
    print(element.text)

flag = 1
if flag == 1:
    ...
    url = 'https://blog.csdn.net/weixin_38648367/article/details/127729489'
    driver.get(url)
    # time.sleep(3)
    # locator = 'name', 'passport_iframe'
    # ele = WW(driver, 5, 0.5).until(EC.visibility_of_element_located(locator))
    # print(ele)
    start = time.time()
    locator = 'xpath',"//button[text()='立即登录']"
    # ele = WW(driver, 2, 0.5).until(EC.visibility_of_element_located(locator))
    ele = driver.find_element(*locator)
    print(ele)
    print('时长：',time.time() - start)
    print(ele)
    ele.click()
    time.sleep(3)
    start = time.time()
    locator = 'css selector',"#passportbox img"
    ele = WW(driver, 2, 0.5).until(EC.visibility_of_element_located(locator))
    print('时长：', time.time() - start)
    print(ele)
    ele.click()


'''doc:内容说明
   1、
   2、 
'''


