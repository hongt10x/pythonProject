# -*- coding: utf-8 -*-
# time: 2023/6/27 14:32
# file: 230627_js操作.py
# author: wht


from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()

# 要想返回到调用原始函数处，按时ctrl+alt+←
test_flag = 1
if test_flag == 1:
    driver.get('http://121.5.150.55:8090/forum.php')
    sleep(1)
    js1 = "document.querySelector('#ls_username').value='admin'"
    driver.execute_script(js1)






sleep(5)
driver.quit()