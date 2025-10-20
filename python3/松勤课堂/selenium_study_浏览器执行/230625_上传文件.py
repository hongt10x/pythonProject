# -*- coding: utf-8 -*-
# time: 2023/6/25 9:43
# file: 230625_上传文件.py
# author: wht

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://42.192.62.8:8088/index.html#/')
driver.find_element('id', 'username').send_keys('sq1')
driver.find_element('id', 'password').send_keys('123')
driver.find_element('id', 'code').send_keys('999999')
driver.find_element('id', 'submitButton').click()
sleep(1)
driver.refresh()
sleep(1)


test_flag = 11
if test_flag == 1: #pywinauto
    driver.find_element('xpath', "//span[text()='文件上传']").click()
    sleep(1)
    driver.find_element('xpath', "//li[contains(text(),'多文件上传（非input）')]").click()
    sleep(1)
    driver.find_element('css selector', ".el-upload-dragger").click()
    sleep(1)
    from pywinauto.keyboard import send_keys
    send_keys(r'D:\PythonStudy\python3\selenium_study\images\1.jpg')
    send_keys('{ENTER}')
    sleep(2)
    send_keys(r'D:\PythonStudy\python3\selenium_study\images\3.jpg')
    send_keys('{ENTER}')
    sleep(2)
    send_keys(r'D:\PythonStudy\python3\selenium_study\images\5.jpg')
    send_keys('{ENTER}')
    # driver.find_element('xpath',"//span[text()='确认上传']").click()


test_flag = 11  #pywin32
if test_flag == 1:
    driver.find_element('xpath', "//span[text()='文件上传']").click()
    sleep(1)
    driver.find_element('xpath', "//li[contains(text(),'单文件上传（非input）')]").click()
    sleep(1)
    driver.find_element('css selector',".el-icon-upload").click()
    sleep(1)
    import win32com.client as wc
    sh = wc.Dispatch('WScript.shell')
    sleep(2)
    sh.Sendkeys(r'D:\PythonStudy\python3\selenium_study\1.jpg' + '\n')


test_flag = 11  #pyautogui
if test_flag == 11:
    driver.find_element('xpath', "//span[text()='文件上传']").click()
    sleep(1)
    driver.find_element('xpath',"//li[contains(text(),'单文件上传（非input）')]").click()
    sleep(1)
    driver.find_element('css selector',".el-icon-upload").click()
    sleep(1)
    import pyautogui
    pyautogui.typewrite(r'D:\PythonStudy\python3\selenium_study\images\4.jpg')
    sleep(1)
    pyautogui.press('Enter')

test_flag = 11
if test_flag == 1:
    # input标签
    driver.find_element('xpath',"//span[text()='文件上传']").click()
    sleep(1)
    driver.find_element('xpath',"//li[contains(text(),'单文件上传')]").click()
    sleep(1)
    driver.find_element('id','cover').send_keys(r'D:\PythonStudy\python3\selenium_study\1.jpg')
    sleep(1)
    # driver.find_element('xpath',"//span[contains(text(),'确定')]").click()
    # sleep(1)
    driver.find_element('css selector',".el-button.el-button--primary.el-button--small").click()
    sleep(1)
    # input('我手工调试吧。。。')
    # driver.find_element('css selector',".el-button.el-button--default.el-button--small.el-button--primary ").click()
    driver.find_element('xpath',"//*[contains(text(),'确定')]").click()




