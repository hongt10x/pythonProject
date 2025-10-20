# -*- coding: utf-8 -*-
# time: 2023/11/24 10:54
# file: _partial-偏函数.py
# author: wht

# def mult(x,y):
#     return x*y
#
# from functools import partial
#
# dou = partial(mult,9)
# print(dou(10))
# print(dou(20))

from functools import partial


def add(*args, **kwargs):
    for _ in args:
        print(_)
    print('-' * 20)
    for k, v in kwargs.items():
        print('%s:%s' % (k, v))
    return sum(args)


#
#
# add123 = partial(add, 1, 2, 3, v1=10, v2=20)
# print(add123(100))
#
# from functools import partial
#
# add_partial = partial(add, 100, k2=20)
# add_partial(11, k3=200)

from functools import partial

def te1st1(x, y, z=100):
    print("%s:%s:%s" % (x, y,z))
    print(x*y*z)
    print("-" * 20)

# partial实现了将初始某些值作为初始值给固定住，不允许后边进行修改
par_test = partial(te1st1, 50,)
print(par_test)
par_test(13,)
par_test(88,99)
#
# alist = ["1", "2", "333","55"]
# blist = [1,3,4,5]
# print("%s" % str(blist))
# print(":".join(alist))

"""对象描述
  
  
"""

# def add1(*args):
#     return sum(args)
#
# add_100 = partial(add1,100)
# print(add_100(1,2,3))


from functools import partial

# 原始函数
def multiply(x, y):
    print(f"x:{x}--y:{y}")
    return x * y

# 使用 partial 固定 y 的值为 5
multiply_by_five = partial(multiply, y=5)

# 使用新的函数
result1 = multiply_by_five(10)  # 相当于 multiply(10, 5)
result2 = multiply_by_five(20)  # 相当于 multiply(20, 5)

print(result1)  # 输出: 50
print(result2)  # 输出: 100