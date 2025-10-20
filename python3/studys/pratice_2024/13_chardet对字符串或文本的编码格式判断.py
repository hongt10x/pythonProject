# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 13_chardet对字符串或文本的编码格式判断.py
@Time    : 2024/5/20 9:57
@Author  : Echo Wang
'''


'''doc:内容说明
   1、chardet 库对单个文件进行编码检测，采用给定文件或字符串数据，通过统计不同字符和n-gram字符频率的方法，计算并返回最可能的编码类型及其可能性。
   2、 
'''

import chardet

# str1 = '中国人'.encode('GB2312')
# print(chardet.detect(str1))

with open('01_property学习.py','rb') as fo:
    print(chardet.detect(fo.read()))

with open('singleton.py','rb') as fo:
    print(chardet.detect(fo.read()))



