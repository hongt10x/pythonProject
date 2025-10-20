# -*- coding: utf-8 -*-
# time: 2023/7/12 10:23
# file: test0712.py
# author: wht
import re

pattern = re.compile('\d')
str1 = '12dad'
# print(dir(pattern))
print(pattern.match(str1).group())
print(re.match(pattern, str1).group())
