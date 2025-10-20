# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : study_2.py
@Time    : 2024/8/22 17:17
@Author  : Echo Wang
'''


count = 10**4
nums = (i for i in range(count))
print(nums)
def check_num(nums):
    if 500 in nums:
        pass


def t1():
    nums = (i for i in range(count))
    check_num(nums)
def t2():
    nums = [i for i in range(count)]
    check_num(nums)


from timeit import timeit

print(f"t1 cost time:{timeit(t1,number=10000)}")
print(f"t2 cost time:{timeit(t2,number=10000)}")