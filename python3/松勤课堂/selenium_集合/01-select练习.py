# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：01-select练习.py
@Date    ：2024/3/16 11:34 
'''
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC


flag = 1
if flag == 1:
    ...
    driver = webdriver.Chrome()
    driver.get('http://sahitest.com/demo/')
    # print(driver.current_url)
    locator = 'Select Test'
    element = driver.find_element('xpath',f"//a[text()='{locator}']")
    # print(element.text)
    element.click()
    time.sleep(1)
    # driver 会跟随浏览器页面的切换自动发生变化，无需重新指定
    # print(driver.current_url)
    # driver.get(driver.current_url)
    locator = '#s1Id'
    select_webelement = driver.find_element('css selector', locator)
    # print(select_webelement.text)
    time.sleep(1)
    locator = '#s1Id>option'
    option_ele = driver.find_elements('css selector', locator)
    # print(option_ele)
    for option in option_ele:
        if option.get_attribute('value'):

        # Select(select_webelement).select_by_value('')
            time.sleep(2)
        # Select(select_webelement).select_by_value()
        # print(option.text)
        # Select(option).select_by_index(1)
        # print(option.get_attribute('value'))
            Select(select_webelement).select_by_value(option.get_attribute('value'))
        # time.sleep(2)


    ...
    driver.quit()

