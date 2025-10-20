# -*- coding: utf-8 -*-
# time: 2023/9/19 10:54
# file: 230919-生成器.py
# author: wht
import random


# from collections import namedtuple
#
# Result = namedtuple('Result', 'count average')
#
#
# def averager():
#     total = 0.0
#     count = 0
#     average = None
#     while True:
#         term = yield
#         if term is None:
#             break
#         total += term
#         count += 1
#         average = total / count
#     return Result(count, average)
#
#
# av = averager()
# try:
#     next(av)
#     print(av.send(9))
#     # av.send(19)
#     # next(av)
# except Exception as res:
#     print(res)
#     # print(res.count)
#
#
# def gen():
#     yield from 'A'
#     # yield from range(1, 4)


# print(gen())
# print(list(gen()))

# eld from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来，对比yield来说代码更加简洁，结构更加清晰。
# def chain(*interables):
#     print(interables, type(interables))
#     for it in interables:
#         yield from it
#
# def chain0(*interables):
#     print(interables, type(interables))
#     for it in interables:
#         for i in it:
#             yield i
#
# s = 'AB'
# t = range(1, 4)
# d = {'k1': 11, 'k2': 22}
# c = chain(s, t, d)
# print(list(c))
#
# print(list(chain0(s, t, d)))

# from collections import namedtuple
#
# ...
# nas = namedtuple('nas','count total')
# a = 1
# b = 2
# n=nas(count=9, total=199)
# n1 = nas(a,b)
# print(n1)
# # n = nas._make([91,100])
# print(n.count)
# print(n.total)
# n=n._replace(count=999)
# print(n.count)
# n=n._asdict()
# print(n)


# from collections import namedtuple
#
# c = {'r': 50, 'g': 205, 'b': 50, 'alpha': 'alpha'}
#
# Cols = namedtuple('Col', c)
# # Cols = namedtuple('Col', {'r': 50, 'g': 205, 'b': 50, 'alpha': 'alpha'})
# print(Cols(**c))
# print(tuple(Cols(**c)))
# b = Cols(r=50, g=200, b=50, alpha=0)
# print(b, b._asdict(), type(b._asdict()))

from collections import  namedtuple
class Person(namedtuple('Student', 'name age city')):
    __slots__ = ()

    @property
    def born_year(self):
        return 2023 - int(self.age)

    def __str__(self):
        return f'Person: 我叫{self.name}, 在{self.city}出生，出生日期{self.born_year}年。'


s = Person('clover', 8, 'Beijing')

# print(s.name)
# print(s)



from collections import namedtuple

Result = namedtuple('Result', 'count average')


# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        # print('term:',term)
        if term is None:
            break
        total += term
        count += 1
        average = total / count
        # print('Result1:',Result(count, average))
        # print(Result(count, average).count,Result(count, average).average)
    return Result(count, average)


# 委派生成器
def grouper(results, key):
    while True:
        results[key] = yield from averager()
        # print("results:",results)


# 客户端代码，即调用方
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        # print('group:',group)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)  # 重要！ ⓬
        # print("results:",results) # 如果要调试，去掉注释
    report(results)
    # 输出报告


def report(results):
    # print('1>>',results)
    # print('2>>',sorted(results))
    for key, result in sorted(results.items()):
        print('key:',key, "result:",result)
        print('result:',result)
        group, unit = key.split(';')
        # print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)


# a = ' hello world '
# print("{!r}".format(a.strip()))
#
# EXPR = [9]
# try:
#     _i = iter(EXPR)
#     print(_i)
# except Exception as e:
#     print(e)
# else:
#     print('bye')
# finally:
#     print('end')


# from random import seed,randint
#
# seed(23)
# print(random.random())
# print(random.random())
# a=10
# while 1:
#     a -=1
#     if a <5:
#         break
#     print('a:',a)
# else:
#     pass
# a=10
# while a >5:
#     a -=1
#     print(a)
# else:
#     print('end')
#
# async def ss:
#     pass


from random import seed, randint

seed(23)

import simpy


class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))
        self.bat_ctrl_proc = env.process(self.bat_ctrl(env))
        self.bat_ctrl_reactivate = env.event()
        self.bat_ctrl_sleep = env.event()

    def drive(self, env):
        """驾驶进程"""
        while True:
            # 驾驶 20-40 分钟
            print("开始驾驶 时间: ", env.now)
            yield env.timeout(randint(20, 40))
            print("停止驾驶 时间: ", env.now)

            # 停车 1-6 小时
            print("开始停车 时间: ", env.now)
            self.bat_ctrl_reactivate.succeed()  # 激活充电事件
            self.bat_ctrl_reactivate = env.event()
            yield env.timeout(randint(60, 360)) & self.bat_ctrl_sleep  # 停车时间和充电程序同时都满足
            print("结束停车 时间:", env.now)

    def bat_ctrl(self, env):
        """电池充电进程"""
        while True:
            print("充电程序休眠 时间:", env.now)
            yield self.bat_ctrl_reactivate  # 休眠直到充电事件被激活
            print("充电程序激活 时间:", env.now)
            yield env.timeout(randint(30, 90))
            print("充电程序结束 时间:", env.now)
            self.bat_ctrl_sleep.succeed()
            self.bat_ctrl_sleep = env.event()


def main():
    env = simpy.Environment()
    ev = EV(env)
    env.run(until=300)

if __name__ == '__main__':
    main()


