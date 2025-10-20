# -*- coding: utf-8 -*-
# time: 2023/11/24 10:45
# file: study_chardet.py
# author: wht

'''doc:内容说明
   1、chardet 库对单个文件进行编码检测，采用给定文件或字符串数据，通过统计不同字符和n-gram字符频率的方法，计算并返回最可能的编码类型及其可能性。
   2、
'''


import chardet
v1 = b"hello world"
print(chardet.detect(v1))

v2 = "仁慈".encode("gbk")
print(chardet.detect(v2))

v3 = "中华小当家".encode("utf8")
print(chardet.detect(v3))

v4 = "123555".encode("utf8")
print(chardet.detect(v4))