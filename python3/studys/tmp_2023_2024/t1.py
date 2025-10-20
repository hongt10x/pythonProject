# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : t1.py
@Time    : 2024/10/25 16:53
@Author  : Echo Wang
'''

# with open("1.log","r",encoding="utf-8") as f:
#     print(f.readline())
#     print(len(f.readlines()))

file = "1.log"
import os
if os.path.isfile(file):
    print("find")
    if os.path.exists(file):
        print("exist")