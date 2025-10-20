# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : good1.py
@Time    : 2025/5/30 16:05
@Author  : Echo Wang
'''
import inspect


class Excle_G01:
    def __init__(self):
        print(self.__class__)
        print(self.__class__.__name__)
        print(self.__class__.__name__.split("_")[-1].lower())
        print(inspect.stack()[0][3])
        print(inspect.stack()[1][3])
