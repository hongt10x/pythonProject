# -*- coding: utf-8 -*-
# time: 2023/8/22 15:00
# file: 4_matplotlib.py
# author: wht
import random

import numpy as np
import matplotlib.pyplot as plt

test_flag = 11
if test_flag == 1:
    ...

    x = np.arange(0, 10, 0.1)
    print(x)
    y = np.sin(x)

    plt.plot(x, y)
    plt.show()

test_flag = 11
if test_flag == 1:
    ...
    x = np.linspace(0, 10, 200)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

test_flag = 11
if test_flag == 1:
    ...
    x = np.arange(10)
    y = np.random.randint(0, 20, 10)
    plt.bar(x, y)
    plt.show()

test_flag = 1
if test_flag == 1:
    ...
    print(random.randint(1,10))
    print(random.random())
    print(random.uniform(1.1,5.4))







