# -*- coding: utf-8 -*-
# time: 2023/6/21 15:25
# file: 230621_基础用法.py
# author: wht


from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

test_flag = 1
if test_flag == 1:
    driver.get('https://www.baidu.com')
    elements = driver.find_elements('xpath', "//*[contains(@class,'hotsearch-item')]")
    for element in elements:
        print(element.text)

test_flag = 11
if test_flag == 1:
    driver.get('https://www.runoob.com/')
    sleep(1)
    ele = driver.find_element('xpath', "//h4[contains(text(),'网站建设指南')]")
    # 滚动方法一
    ele.location_once_scrolled_into_view
    # 滚动方法二
    # ActionChains(driver).scroll_to_element(ele).perform()
    # sleep(3)
    # ele.click()
    print(ele.value_of_css_property('font-size'))
    print(ele.value_of_css_property('color')) #rgba(100, 133, 76, 1)


test_flag = 11
if test_flag == 1:
    driver.get('http://121.5.150.55:8090/forum.php')
    driver.find_element('css selector',".pn.vm").click()
    sleep(3)
    driver.refresh()
    sleep(3)
    driver.find_element('css selector','.pn.vm').find_element('css selector','em').click()
