# # -*- coding: utf-8 -*-
# # time: 2023/8/28 9:52
# # file: test230828.py
# # author: wht
#
# def add(*args):
#     return sum(args)
#
#
# # print(add(1,3,4) + 100)
#
# # print(sum([3,4]))
#
# from functools import partial
#
# add_100 = partial(add, 100)
#
# # print(add_100(1, 2, 3))
#
# #
# # def make_averager():
# #     count = 1
# #     total = 1
# #
# #     def averager(new_value):
# #         nonlocal count, total
# #         count += 1
# #         total += new_value
# #         return total / count
# #     print(f'count:{count},total:{total}')
# #     return averager
# #
# #
# # for i in range(3, 7):
# #     print(i,make_averager()(i))
#
#
# # def x():
# #     x = 111
# #     def y():
# #         # print(x)
# #         nonlocal x
# #         x = 100
# #         print(x)
# #     print(x,...)
# #     return y
# # x()()
#
# import time
#
#
# def clock(func):
#     def clocked(*args):
#         t0 = time.perf_counter()
#         result = func(*args)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         arg_str = ', '.join(repr(arg) for arg in args)
#         print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
#         return result
#
#     return clocked
#
#
# from functools import lru_cache
#
#
# @lru_cache()
# @clock
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# #
# # if __name__ == '__main__':
# #     print(fibonacci(6))
#
# # clockdeco_demo.py
#
# # import time
# import functools
#
#
# # @functools.lru_cache()
# # @clock
# # def snooze(seconds):
# #     time.sleep(seconds)
# # @functools.lru_cache()
# # @clock
# # def factorial(n):
# #     return 1 if n < 2 else n*factorial(n-1)
# #
# # if __name__=='__main__':
# #     print('*' * 40, 'Calling snooze(.123)')
# #     snooze(.123)
# #     print('*' * 40, 'Calling factorial(6)')
# #     print('6! =', factorial(6))
#
#
# # a = (1,1,3,1,)
# # print(a.count(1))
# # print(a.index(1))
# # print(a.__add__((9,)))
# # print(a)
#
#
# class Demo:
#     @classmethod
#     def klassmeth(cls, *args):
#         return args
#
#     @staticmethod
#     def statmeth(*args):
#         return args
#
#
# # de = Demo()
# # print(de.klassmeth(1,3))
# # print(de.klassmeth('span'))
# # print(de.statmeth(123, 3))
# # print(de.statmeth('span'))
# #
# # ms = ('127.0.0.1',8080)
# # mk = 'messages'
# # print(f'{mk:$<15} -- messsges')
# # print(f'{mk:$^15} -- messsges')
# # # # width = 10
# # # print(f'{mk:$^{0}} -- messsges'.format(width=100))
# # a= 0.9777333
# # print(format(a, '.1%'))
# #
# # list
# # a = [x for x in range(3,0,-1)]
# # print(a)
# # print(all(a,))
#
# # None 的真假值是 False
# # print(bool(None))
# # 输出 False
#
# # 一个空字符串（""）的真假值是 False
# # print(bool(""))
# # 输出 False
#
# # 一个空字符串或任何可迭代对象的真假值是 False
# # print(bool([]))
# # 输出 False
#
# # 0 {int (0), float (0.0) 和 complex (0j)} 的真假值是 False
# # print(bool(0))
# # 输出 False
#
#
# #
# # a = [x for x in range(0,3,1)]
# # print(all(a))
# # print(any(a))
# # b = 'bbds123sse'
# # print(b.isdigit())
# # c = '1234'
# # if all([a,  b]):
# #     print('find...')
# # else:
# #     print('cannot find')
#
#
# # def f1(x):
# #     return x*2
# # def f2(x,y):
# #     print(x,y)
# #     return x*y
# # from functools import reduce
# # print(list(map(f1, range(1,10))))
# #
# #
# # print(reduce(f2,range(1,10)))
# #
# # print(reduce(lambda x,y:x+y,range(100)))
#
# my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
# print([sub[1] for sub in my_list])
# import functools
#
# # functools.reduce(lambda a, b: a+b, [sub[1] for sub in my_list])
# print(functools.reduce(lambda a, b: a + b[1], my_list, 0))
#
#
# # print(my_list.__getitem__(1))
#
# # l1 = [1,3,5,6,7,8]
# # import random
# # random.shuffle(l1)
# # print(l1)
#
# class C: pass
#
#
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# print(issubclass(A, B))
# print(issubclass(B, A))
# # B是A的子类
#
# print(isinstance(A, object))
#
#
# import collections
#
# Card = collections.namedtuple('Card', ['rank', 'suit'])
#
#
# class FrenchDeck2(collections.MutableSequence):
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#     print(ranks)
#     print(suits)
#     def __init__(self):
#
#         self._cards = [Card(rank, suit) for suit in self.suits
#                        for rank in self.ranks]
#         print(self._cards)
#
#     def __len__(self):
#
#         return len(self._cards)
#
#     def __getitem__(self, position):
#
#         return self._cards[position]
#
#     def __setitem__(self, position, value):  # ➊
#
#         self._cards[position] = value
#
#     def __delitem__(self, position):  # ➋
#
#         del self._cards[position]
#
#     def insert(self, position, value):  # ➌
#
#         self._cards.insert(position, value)
#
# fr = FrenchDeck2()
import time


def wapper(ar):
    print(f'...{ar}...')

    def innerwapper(fun):
        def inner(*args, **kwargs):
            print('开始休眠...')
            print(f'...{ar}...')
            time.sleep(2)
            fun(*args, **kwargs)

        return inner

    return innerwapper


# @wapper('test')
def func1(x):
    print('...func1...')
    print(f'...{x}...')


# func1('goodbye')


l1 = [1, 3, 5, 7]


# print(l1.pop())
# print(l1)
# l1.remove(5)
# print(l1)


def f1(x: str) -> None:
    print(f'{x}')
    return 999


# print(f1('9'))

# a:int= 3
# print(a)

def f2(x: str):
    print(f'{x}')
    return 999


def demo1(name: str, age: 'int >0' = 20) -> str:
    print(f'name:{name}')
    print(f'age:{age}')
    return f'hello {name}'


# print(demo1('王先生', 25))
# print(demo1('王先生'))


def demo2(name: any, age: 'int >0' = 20) -> str:
    print(f'name:{name}')
    print(f'age:{age}')
    return f'hello {name}'


# print(demo2(999))


class A:
    def __init__(self):
        print(f'A: {self.__class__.__name__}')


class B(A):
    def __init__(self):
        print(f'B: {self.__class__.__name__}')


# b = B()

class Test:
    def __init__(self):
        self.a = 1

    def fuc1(self, x, y):
        print(x + y)


# test = Test()
# test.fuc1(1,2)
# test.fuc1 = lambda self,x,y:print(x +y*2 + self.a)
# test.fuc1(test,1,2)


# Test.fuc1 = lambda self,x,y: print(x+y*2+self.a)
# test = Test()
# test.fuc1(1,1)


import abc


class Good(abc.ABC):
    @abc.abstractmethod
    def price(self):
        print(f'This is price of God ...')

    @abc.abstractmethod
    def price1(self):
        print(f'This is price1 of God ...')


class Food(Good):
    def price1(self):
        print(self, 100000)
        print("{} price:$4".format(__class__.__name__))

    def price(self):
        print("{} price:$5".format(__class__.__name__))


class Clothes(Good):
    def price1(self):
        print(self)
        Food().price1()
        print(self)
        print(f"{self.__class__.__name__} 's price1")

    def price(self):
        print("{} price:$5".format(__class__.__name__))


# print(Clothes)
# print(Clothes())
# # Food().price1()
# Clothes().price()
# Clothes().price1()
# print(Clothes.__mro__)

# class Displayer(object):
#     def display(self, message):
#         print ("into Displayer display")
#         print (self)
#         print(message)
# class LoggerMixin(object):
#     def log(self, message, filename='logfile.txt'):
#         print ("into LoggerMixin log")
#         with open(filename, 'a') as fh:
#             fh.write(message)
#      def display(self, message):
#         print ("into LoggerMixin display")
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message):
#         print('into MySubClass log')
#         super().log(message,filename='subclasslog.txt')
#
# subclass = MySubClass()
# subclass.display('This string will be shown .....')

# with open('1.log','r') as ff:
#     # print(len(ff.readlines()))
#     with open('1.log','a+') as fk:
#         # print(fk.seek())
#         # fk.write('abc'+'\n')
#         # fk.write('abc'+'\n')
#         # fk.write('abc')
#         fk.seek(2,0)
#         print(len(fk.readlines()))
#     # print(len(ff.readlines()))

# with open('1.log','rb') as fd:
#     fd.seek(1,0)
#     print(fd.tell())
#     print(fd.seek(-1, 2))
#     print(fd.tell())
#     # print(fd.read())
#     # fd.write('badman')
#     # print(fd.read())


# class Bar(object):
#   def __init__(self, a):
#     self.a = a
#
# class BarSlotted(object):
#   __slots__ = "a"
#   def __init__(self, a):
#     self.a = a
#
# # create class instance
# bar = Bar(1)
# print(bar.a)
# bar_slotted = BarSlotted(1)
# print(bar_slotted.b)

# __slots__在继承中有两种表现：
#
# 1. 子类未声明__slots__时，不继承父类的__slots__，即此时子类实例可以随意赋值属性
#
# 2. 子类声明__slots__时，继承父类的__slots__，即此时子类的__slots__为其自身+父类的__slots__

# class Class1:
#     # __slots__ = ('age','name')
#     pass
# class Stu(Class1):
#     # __slots__ = ('sex',)
#     __slots__ = ()
#     pass
# stu = Stu()
# print(stu.__dir__())
# stu.age = 'wang'
# stu.sex = '222'
# stu.gend = 'look'


import re
import reprlib

# RE_WORD = re.compile('\W+')
RE_WORD = re.compile('\w+?')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # def __iter__(self):
    #     for word in self.words:  # ➊
    #         yield word  # ➋
    #     return
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


# sen = Sentence('882-k3md=ma,f')
# print(sen.__iter__())
# print(list(sen.__iter__()))

# print("顶级编程语言是 %s, %r" % ('Py', 'C++'))
# print('顶级编程语言是 {!r},{!r}'.format('Py','C++'))
# print('顶级编程语言是 {!r}'.format(999))
#
# a = 5
# print(1 == a < 2)
# print(2 < 3 < 6 > a)

# import re
# patten = re.compile('\w+')
#
# res = patten.findall('23,d11-d')
# print(res)


import itertools

# a1 = itertools.islice([1, 3, 4,5], 3)
# print(list(a1))

# 无限迭代器
# count([start=0, step=1]) 接收两个可选整形参数，第一个指定了迭代开始的值，第二个指定了迭代的步长。
# for i in itertools.count(10,2):
#     print(i)
#     if i>20:break


# cycle(iterable) 是用一个可迭代对象中的元素来创建一个迭代器，并且复制自己的值，一直无限的重复下去。
# num = 0
# for i in itertools.cycle('abcd'):
#     print(i)
#     num += 1
#     if num == 10:break

# repeat(elem [,n])是将一个元素重复n遍或者无穷多遍，并返回一个迭代器。
# for i in itertools.repeat('abcd',5):
#     print(i)

# 笛卡儿积
# for i in itertools.product([1,2,3],[4,5,6]):
#     print(i)
#
# print(tuple(zip([1,2,3],[4,5,6])))
# print(list((x,y) for x in [1,2,3] for y in [4,5,6]))

# 排列
# for i in itertools.permutations('abc'):
#     print(i)
# 组合
# combinations(iterable,r) 返回的是可迭代对象所有的长度为 r 的子序列，注意这与前一个函数 permutation 不同，permutation 返回的是排列，而 combinations 返回的是组合。
# for i in itertools.combinations('abc',2):
#     print(i)

# combinations_with_replacement(iterable, r) 返回一个可与自身重复的元素组合，用法类似于 combinations 。
# for i in itertools.combinations_with_replacement('abc',2):
#     print(i)

# chain(*iterables) 可以把多个可迭代对象组合起来，形成一个更大的迭代器。
# for i in itertools.chain('good','bye'):
#     print(i)

# groupby(iterable,key=None) 可以把相邻元素按照 key 函数分组，并返回相应的 key 和 groupby，如果key函数为 None，则只有相同的元素才能放在一组。
# for key,group in itertools.groupby('AaaabBBbBccCCd',lambda u:u.upper()):
#     print(list(group))

# groupby(iterable,key=None) 可以把相邻元素按照 key 函数分组，并返回相应的 key 和 groupby，如果key函数为 None，则只有相同的元素才能放在一组。
# for i in itertools.accumulate([1,2,3,4,5]):
#     print(i)

# 如果我们指定这个累计函数，则还能有不同的用法，例如，指定一个最大值函数，或者自己定义的函数。

# for i in itertools.accumulate([5, 3, 4, 6, 67, 7], max):
#     print(i)


# for i in itertools.accumulate([5, 3, 4, 6, 67, 7], lambda x,y: x if x >y else y):
#     print(i)

# for i in itertools.permutations('aaa'):
#     print(i)

# a='d11'
# a = [1,2, 3]
# print('此处数据：{!r}'.format(a))
#
# def smiple_coroutine():
#     print('-> coroutine start...')
#     x = yield
#     print('-> coroutine:',x)
#
# sm = smiple_coroutine()
# print(sm)
# # print(next(sm))
# # 首先要调用 next(...) 函数，因为生成器还没启动，没在 yield 语
# # 句处暂停，所以一开始无法发送数据
# # sm.send('start')
# sm.send('goodbye')
#

#
# def smiple_coroutine2(a):
#     print('-> start a:',a)
#     b = yield a
#     print('-> received:b',b)
#     c = yield a + b
#     print('-> Received c:',c)
#     d = yield b + c
#     print('-> received:d',d)
#
# my_coro2 = smiple_coroutine2(10)
# from inspect import getgeneratorstate as gt
#
# print(gt(my_coro2))
# print(next(my_coro2))
# print(gt(my_coro2))
# print(my_coro2.send(19))
# print(gt(my_coro2))
# print(my_coro2.send(99))
# print(gt(my_coro2))
# try:
#     print(my_coro2.send(100))
# except:
#     print(gt(my_coro2))


# from functools import wraps


from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# av = averager()
# try:
#     next(av)
#     av.send(9)
#     av.send(19)
#     next(av)
# except Exception as res:
#     print(res)

def gen():
    yield from 'AB'
    yield from range(1,4)

print(gen())
print(list(gen()))



