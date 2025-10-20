# -*- coding: utf-8 -*-
# time: 2023/6/25 17:11
# file: 230625_显式等待.py
# author: wht

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, ctime,time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://121.5.150.55:8090/forum.php')

test_flag = 1
if test_flag == 1:
    y = ('css selector', '#ls_username')
    WW(driver, 5, 0.5).until(lambda x: x.find_element(*y)).send_keys('admin')

test_flag = 11
if test_flag == 1:
    locator = ('css selector', '#ls_username')
    WW(driver, 5, 0.5).until(EC.presence_of_element_located(locator)).send_keys('admin')


test_flag = 11
if test_flag == 1:
    ele_username = driver.find_element('css selector', '#ls_username')
    print("开始: ",ctime(),time())
    locator = ('css selector', '#ls_username')
    WW(driver,5,0.5).until(EC.visibility_of_element_located(locator)).send_keys('admin')