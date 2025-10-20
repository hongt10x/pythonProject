# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : test09.py
@Time    : 2024/12/20 9:04
@Author  : Echo Wang
'''


import copy

# n1 = {"k1":"v1","k2":['repo',1234]}
# n2 = copy.copy(n1)
# print(id(n1),id(n2))
# print(id(n1['k1']),id(n2['k1']))
# print(id(n1['k2']),id(n2['k2']))
# print("="*27)
# n2['k2'].append(999)
# print(id(n1['k1']),id(n2['k1']))
# print(id(n1['k2']),id(n2['k2']))
# print(n1, n2)
# print("*"*27)
#
# n3= copy.deepcopy(n1)
# print(id(n1),id(n3))
# print(id(n1['k1']),id(n3['k1']))
# print(id(n1['k2']),id(n3['k2']))
# print("="*27)
# n3['k2'].append(999)
# print(id(n1['k1']),id(n3['k1']))
# print(id(n1['k2']),id(n3['k2']))
# print(n1, n3)
# flag = 0
# a = flag if flag else 1
# print(a)

# def f1():
#     a= 25
#     def f2(x):
#         return a*x*2
#     # return f2
#     print(f2(2))
#
# a =100
# # print(f1()(2))
# f1()


# import chardet
#
# print(chardet.detect(b"Hello"))
# print(chardet.detect("中国人，中国心".encode("gbk")))
# print(chardet.detect("中国人，中国心".encode("utf8")))
# print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))
#
#
# print(b"xxx"==u"xxx")
#
# print("xxx".encode("utf8")=="xxx".encode("gbk"))
# print(chardet.detect("xxx".encode("utf8")))
# print(chardet.detect("xxx".encode("gbk")))
# print(chardet.detect("中国",error="ingnore"))



# with open("1.yml",'r') as f:
#     chunks = f.read(1024*8)
# with open("1.txt",'wb') as f:
#     for chunk in chunks:


# while (v:= 5/2 == 0):
#     print('xxxx')

import re
a = '1.1.1.1;2.2.2.2,3.3.3.3'
b = re.split(r'[,;]',a)
print(b)


