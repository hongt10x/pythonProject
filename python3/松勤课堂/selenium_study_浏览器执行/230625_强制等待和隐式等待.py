# -*- coding: utf-8 -*-
# time: 2023/6/25 14:55
# file: 230625_强制等待和隐式等待.py
# author: wht

...
'''内容说明
1. ele_username.get_attribute("placeholder") 返回空或""
2. ele_username.get_attribute("placeholde") 元素名写错，则返回None

'''

from selenium import webdriver
from time import sleep, ctime,time

driver = webdriver.Chrome()
# 最大超时时间5s  ,Amount of time to wait (in seconds),只设置一次全局生效
driver.implicitly_wait(65)
driver.maximize_window()
driver.get('http://121.5.150.55:8090/forum.php')

test_flag = 1
if test_flag == 1: #解决隐式等待的缺陷，增加轮询处理
    max_wati_time= 105
    start_time = time()
    end_time = max_wati_time+start_time
    freq_time = 2
    ele_username = driver.find_element('css selector', '#ls_username')
    print("开始: ",ctime(),time())
    while True:
        if ele_username.get_attribute("placeholder"):
            print(ele_username.get_attribute("placeholder"))
            break
        if time() > end_time:
            print('超时退出')
            break
        sleep(freq_time)
        print('等待2s...')
    print("结束: ",ctime())


test_flag = 11
if test_flag == 1: #隐式等待的缺陷，不支持动态属性
    ele_username = driver.find_element('css selector', '#ls_username')
    print(f'xx{ele_username.get_attribute("placeholder")}xx')

test_flag = 11
if test_flag == 1: #隐式等待，手工调试
    try:
        print('开始找元素:', ctime())
        driver.find_element('css selector', '.pn.vm').click()
        driver.find_element('css selector', "[id^=username1]").send_keys('admin')
    except:
        print('异常，当前时间:', ctime())
    finally:
        print('最终时间:', ctime())

test_flag = 11
if test_flag == 1:  # 隐式等待
    driver.find_element('css selector', '.pn.vm').click()
    driver.find_element('css selector', "[id^=username]").send_keys('admin')

test_flag = 11
if test_flag == 1:  # 强制等待
    # driver.get('http://121.5.150.55:8090/forum.php')
    driver.find_element('css selector', '.pn.vm').click()
    sleep(1)
    # driver.find_element('xpath', '//input[starts-with(@id,"username_")]').send_keys('admin')
    # driver.find_element('xpath','//input[contains(@id,"username")]').click()
    driver.find_element('css selector', "[id^=username]").send_keys('admin')
