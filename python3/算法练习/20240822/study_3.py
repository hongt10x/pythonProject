# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : study_3.py
@Time    : 2024/8/22 17:27
@Author  : Echo Wang
'''


# a = [1,2,3]
# b = [4,5,6]
# b.extend(a)
# print(b)
# c = (_ for _ in b)
# print(c)

# for i in range(10):
#     if i == 10:
#         break
# else:
#     print("cannot find...")

flag = 11
if flag == 1:
    ...

    count = 10**4

    def check_num(nums):
        if 500 in nums:
            pass


    def t1():
        nums = (i for i in range(count))
        check_num(nums)
    def t2():
        nums = [i for i in range(count)]
        check_num(nums)
    import profile,cProfile

    cProfile.run('t1()')
    cProfile.run('t2()')


flag = 11
if flag == 1:
    ...
    from random import randrange
    # print(randrange(10000))
    L = [randrange(10000) for _ in range(10000)]
    S = set(L)

    def t11():
        # S = set(L)
        if 42 in L:
            pass

    def t22():
        # S = set(L)
        if 42 in S:
            pass


    from timeit import timeit

    print(f"t11 cost time: {timeit(t11,number=10000)}")
    print(f"t22 cost time: {timeit(t22,number=10000)}")

flag = 11
if flag == 1:
    ...
    lists = [[7,8,13,2,3,4,32,3,3,4,3,3,2,23,4,3,5,6,6,5,77,321],[7,8,13,2,3,4,32,3,3,4,3,3,2,23,4,3,5,6,6,5,77,321],[7,8,13,2,3,4,32,3,3,4,3,3,2,23,4,3,5,6,6,5,77,321],[7,8,13,2,3,4,32,3,3,4,3,3,2,23,4,3,5,6,6,5,77,321],[7,8,13,2,3,4,32,3,3,4,3,3,2,23,4,3,5,6,6,5,77,321]]
    a = sum(lists,[])
    print(a)

    def t12():
        a = sum(lists, [])
    def t13():
        res = []
        for i in lists:
            res.extend(i)
    from timeit import timeit
    print(f"t12 cost time: {timeit(t12,number=10000)}")
    print(f"t13 cost time: {timeit(t13,number=10000)}")

    # t12 cost time: 0.00921630000000001
    # t13 cost time: 0.00697819999999999

    print(1.01**100)

flag = 1
if flag == 1:
    ...
    board = [[0]*8 for i in range(8)]
    print(type(board),board)
    import time
    print(time.time())
    print(int(time.time()))

    t1 = {i for i in range(10)}
    print(type(t1),t1)

    t2 = (i for i in range(10))
    print(type(t2), t2)







