# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : test04.py
@Time    : 2025/1/15 9:57
@Author  : Echo Wang
'''


def t1(i):
    i = 10

    def t2():
        i = 100
        print(i)
        # i=200

    print(i)

    def add():
        nonlocal i
        i += 1
        print(i)

    return t2, add


# t, add_ = t1(100)
# t()
# add_()

def f1():
    a =100
    print(id(a))
    def f2():
        print(a)
    return f2


print(f1().__closure__)