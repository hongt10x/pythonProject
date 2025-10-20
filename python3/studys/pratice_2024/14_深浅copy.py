# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 14_深浅copy.py
@Time    : 2024/5/20 13:55
@Author  : Echo Wang
'''


import copy

a = [1,3,(2,4),[5,6,[7,8]]]

b = copy.copy(a)
c = copy.deepcopy(a)
print(a)
print(b)
print(c)
a[0] = 999
a[3].append(10)
print(a)
print(b)
print(c)
a[3][2].append(9)
print(a)
print(b)
print(c)


