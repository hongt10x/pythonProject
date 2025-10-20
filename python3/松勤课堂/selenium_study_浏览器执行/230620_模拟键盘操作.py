# -*- coding: utf-8 -*-
# time: 2023/6/19 14:32
# file: 230620_模拟键盘操作.py
# author: wht



# //*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em
#
# /html/body/div[5]/div/div[1]/form/div/div/table/tbody/tr[2]/td[3]/button/em
#
# //*[starts-with(@class,'s_form_wrapper')]

import os
from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.maximize_window()

test_flag = 1
if test_flag == 1:
    driver.get('https://www.baidu.com')
    sleep(1)
    driver.find_element('css selector','#s-top-loginbtn').click()
    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__changeSmsCodeItem').click()
    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__changePwdCodeItem').click()
    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__userName').send_keys('admin')
    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__userName').send_keys('ctrl','a')
    driver.find_element('css selector','#TANGRAM__PSP_11__userName').send_keys('ctrl','a')

    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__userName').send_keys(Keys.RIGHT,'1')
    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__userName').send_keys(Keys.RIGHT,'2')
    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__userName').send_keys(Keys.LEFT,'3')
    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__userName').send_keys(Keys.CONTROL,'c')
    driver.find_element('css selector','#TANGRAM__PSP_11__password').send_keys(Keys.CONTROL,'v')
    sleep(1)
    driver.find_element('css selector','#TANGRAM__PSP_11__password').send_keys('123')


# test_flag = 1
# if test_flag == 1:
#     driver.get('http://www.baidu.com')




sleep(30)
os.system('taskkill /im chromedriver.exe /F')



