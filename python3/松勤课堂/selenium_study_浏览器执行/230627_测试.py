# -*- coding: utf-8 -*-
# time: 2023/6/27 15:39
# file: 230627_测试.py
# author: wht

def func1(a,*arg):
    print(a,type(a))
    print(arg,type(arg))
    print(list(arg),type(list(arg)))

func1(1,3,5)