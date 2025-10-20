# -*- coding: utf-8 -*-
# time: 2023/8/22 10:39
# file: 2_numpy.py
# author: wht

import numpy as np
test_flag = 11
if test_flag == 1:
    ...
    print('123')
    # a = np.array([1,3,4,5])
    # print(a,type(a))

    b = np.zeros(10)
    print(b)
    print(np.ones(10))
    print(np.arange(5))
    print(np.arange(1,10,2))
    print(np.linspace(3,15,3,retstep=True))

test_flag = 1
if test_flag == 1:
    ...
    a = np.arange(5)
    b = a[1:3:1]
    print(a)
    print(b)
    print(a[:3])
    print(a[...,2:])
