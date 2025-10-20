# -*- coding: utf-8 -*-
# time: 2023/6/13 14:20
# file: 230621_模拟滚动.py
# author: wht

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()


test_flag = 1
if test_flag == 1:
    driver.get('http://www.baidu.com')
    sleep(1)
    driver.find_element('css selector','#kw').send_keys('python \n')
    sleep(1)

    print(driver.find_element('css selector','html').text)
    # driver.back()
    # sleep(1)
    # driver.forward()
    # sleep(1)
    # driver.refresh()

    # ele_other = driver.find_element('xpath',"//a[@class='n']")
    # ActionChains(driver).scroll_to_element(ele_other).perform()

    # ActionChains(driver).scroll_by_amount(0,1000).perform()
