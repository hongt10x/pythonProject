# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : study_1.py
@Time    : 2024/8/22 15:58
@Author  : Echo Wang
'''

from timeit import timeit
from threading import Thread

count = 10 ** 3

def check_num(nums):
    it = 500
    if it in nums:
        return it
def t1():
    nums = []
    for i in range(count):
        nums.append(i)
    # print(nums)
    nums.reverse()
    check_num(nums)


# print(nums)
def t2():
    nums = []
    for i in range(count):
        nums.insert(0, i)
    # print(nums)
    check_num(nums)


def t3():
    nums = [i for i in range(count)]
    nums.reverse()
    check_num(nums)


def t4():
    nums = (i for i in range(count))
    x = check_num(nums)
    # print(f"x:{x}")
    # nums = [j for j in nums]
#

print(f"t1 cost time: {timeit(t1, number=1000)}")
print(f"t2 cost time: {timeit(t2, number=1000)}")
print(f"t3 cost time: {timeit(t3, number=1000)}")
print(f"t4 cost time: {timeit(t4, number=1000)}")

# 10**5
# t1 cost time: 0.004896499999999998
# t2 cost time: 1.7003221000000002
# 10**6
# t1 cost time: 0.06477330000000003
# t2 cost time: 298.2327336
