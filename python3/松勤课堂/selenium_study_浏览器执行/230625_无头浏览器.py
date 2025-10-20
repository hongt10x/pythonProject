# -*- coding: utf-8 -*-
# time: 2023/6/25 17:45
# file: 230625_无头浏览器.py
# author: wht
import time

# print(time.time())
# print(time.monotonic())
#
# # import os
#
# try:
#     os.makedirs('a/b')
#     b=2/0
#     print('a')
# except Exception as e:print(e)


# a = [1,3,5,7]
# for _ in a:
#     if _ == 5:
#         a.remove(_)
#         # a.pop()
# print(a)


from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.maximize_window()

test_flag = 1
if test_flag == 1:
    driver.get('http://www.baidu.com')



test_flag = 1
if test_flag == 1:
    driver.get('http://www.baidu.com')
    ele1 = driver.find_element('id','kw')
    ele1.send_keys('good test')
    print(ele1.get_attribute('value'))
    print(ele1.text)

test_flag = 1
if test_flag == 1:
    driver.get('http://sahitest.com/demo/selectTest.htm')
    ele_options = driver.find_element('css selector','#testInputEvent')
    ele_options2 = driver.find_element('css selector','#s1')

    # print(ele_options.text)
    # print(ele_options.get_attribute('value'))
    # print(ele_options.tag_name)
    # print(ele_options)
    # print(ele_options.is_displayed())
    # print(ele_options.is_selected())
    # print(ele_options.is_enabled())
    # print(ele_options.text)
    # print(ele_options.location_once_scrolled_into_view)
    # print(ele_options2.is_displayed())
    # print(ele_options2.is_selected())
    # print(ele_options2.is_enabled())

    # ele_options3 = driver.find_element('xpath',"//*[contains(text(),'Option 2')]")
    # print(ele_options3.tag_name)

# dic = {}
# dic.update(a='b')
#
# print(dic)
driver.quit()