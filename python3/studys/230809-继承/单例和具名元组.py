# -*- coding: utf-8 -*-
# time: 2023/8/9 9:59
# file: 单例和具名元组.py
# author: wht

# class Single_Instance:
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#         return cls.instance
#
#     def fun(self, a, b):
#         return a * b
#
#
# a = Single_Instance()
# print(a, id(a))
# b = Single_Instance()
# print(b, id(b))
# a.name = "good"
# print(b.name)

'''
# print(a.fun(2, 3))
# #
# # import logging
# #
# # print(logging.debug(b))
# #
# # import subprocess
# # subprocess.Popen
# #
# #
# # '''
# # from functools import reduce
# #
# # # kwargs = {'universal_newlines':999}
# # # kwargs = {}
# # # kwargs['input'] = 'xxx' if kwargs.get('universal_newlines', False) else b''
# # # print(kwargs)
# #
# #
# # # def func1(*args,**kwargs):
# # #     print('args: {}; kwargs: {}'.format(args,kwargs))
# # #
# # # func1('a','b',c=99)
# # #
# # #
# # # print(''.join(('9','8','5')))
# #
# #
# # # l1 = [1,3,5,7,9]
# # # l2 = [2,4,6,8,0,10]
# # # l12 = [11,33,55,77,99]
# # #
# # # print(list(zip(l1,l2,l12)))
# # #
# # # # __func__ = property(lambda self: object(), lambda self, v: None, lambda self: None)
# # # a=999
# # # print(lambda l1: object())
# #
# # #
# from random import choice
# l1 = [1,3,5,7,9]
# print(choice(l1))
# # #
import functools
# print((1,3)+(2,4))
#
# symbols = '$¢£¥€¤中'
# print([ord(symbol) for symbol in symbols])
# #
# # x = [1, 3, 5, 7, 9]
# # # dump = [ord(str(x)) for x in x]
# # # print(x)
# #
# # # def func(x):
# # #     for x in x:
# # #         print(x)
# # # func(x)
# # #
# # # for x in x:
# # #     print(x)
# #
# # # s = filter(lambda y: y % 2 != 0, x)
# # # for i in s:
# # #     print(i)
# #
# # l = [1, 2, 3, 4]
# # # print(list(map(lambda x: x>2, l)))
# # # print(list(filter(lambda x: x>2, l)))
# # m = ['a', 'b', 'c', 'f']
# # # zip_l_m = list(zip(l,m))
# # # print(zip_l_m)
# # # # 使用*逆过程/
# # # print(list(zip(*zip_l_m)))
# #
# # # print(reduce(lambda x,y:x*y, l,m))
# # #
# # #
# # # names = ['www','gggg','tttt',]
# # # print('{} {} {}'.format(*names))
# # #
# # #
# # #
# # # import collections
# # # Card = collections.namedtuple('Card',names)
# # # print(Card.)
# #
# # import subprocess
# #
# # # board = [['_'] * 3 for i in range(3)]
# # # print(board)
# # # board[1][2] = 0
# # # print(board)
# # #
# # # board1 = [['_'] * 3] * 3
# # # print(board1)
# # # board1[1][2] = 0
# # # print(board1)
# # # print([1,3] + [4,6])
# # #
# # # t = (1,2,[30,40])
# # # print(t)
# # # print(t[2] ,type(t[2]))
# # # t[2] += [50,60]
# # #
# # # t[2].extend([70,80])
# # #
# # # print(t[2])
# # # print(t)
# #
# # import bisect
# #
# # import bisect
# # import sys
# #
# # HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# # NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# # ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
# #
# #
# # def demo(bisect_fn):
# #     for needle in reversed(NEEDLES):
# #         position = bisect_fn(HAYSTACK, needle)
# #         offset = position * ' |'
# #         print(ROW_FMT.format(needle, position, offset))
# #
# #
# # if __name__ == '__main__':
# #     if sys.argv[-1] == 'left':
# #         bisect_fn = bisect.bisect_left
# #     else:
# #         bisect_fn = bisect.bisect
# #     print('DEMO:', bisect_fn.__name__)
# #     print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
# #     demo(bisect_fn)
# #
# #
# from collections import namedtuple
# Movie = namedtuple('Movie', ('name', 'released', 'director'))
# movies = [
#     Movie('Jaws', 1975, 'Spielberg'),
#     Movie('Titanic', 1997, 'Cameron'),
#     Movie('The Birds', 1963, 'Hitchcock'),
#     Movie('Aliens', 1986, 'Cameron')
# ]
# print(movies)
# print(movies[0].name)
# # a = input("请输入：")
# #
# #
# # ++++
# # # def add1(x,y):
# #     return x+y+3
# # def del1(x,y):
# #     return x-y
# #
# # dic = {'autoadd':add1,'autodel':del1}
# # print(dic)
#
#
#
#
# class A:
#     a =10
#     class B:
#         a =20
#         print(a)
#     def test.robot(self):
#         class C:
#             a =1100
#
#     b = B()
#     print(b.a)
#
#
# a1 = A()
#
#
#
#
#
#
#
#
#


import time

start = time.time()
time.sleep(3)
print(time.time() - start)

#
#
#
