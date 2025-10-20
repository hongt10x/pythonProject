# coding: utf8
# 03-路径处理.py
# 2024/3/11

import pathlib


# path1 = pathlib.Path('/root','./home')
# print(path1)
# path2 = pathlib.Path('/root/','./home').resolve()
# print(path2)


from selenium import webdriver
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
# webdriver
drive.get("http://www.baidu.com")
# print(dir(drive))
with open('webDriver.md','w',encoding='utf8') as f:
    for _ in dir(drive):
        if _[0] != "_":
            print(_)
            f.write(_)
            f.write('\n')

drive.close()
# eles = drive.find_element('css selector','kw')
#
#
# # webElement
# for _ in dir(eles):
#     if _[0] != "_":
#         print(_)




