# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 16_验证.py
@Time    : 2025/1/3 10:46
@Author  : Echo Wang
'''


l1 = [1,3,5]
k = []
for i in l1:
    print(i)
    k.append(i) if i > 2 else k


print(k)
try:
    s = 10/0
except Exception as e:
    print(e)
