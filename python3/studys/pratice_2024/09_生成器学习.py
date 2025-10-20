# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：09_生成器学习.py
@Date    ：2024/4/22 16:38 
'''


flag = 1
if flag == 1:
    ...

    def f1():
        yield 'A'


    print(f1())
    print(next(f1()))
    print(next(f1()))



flag = 1
if flag == 1:
    ...

    '''内容说明
        1、你尝试的这种写法`f = lambda : yield`实际上是创建了一个匿名函数，但是你没有指定这个函数在每次迭代时应该生成什么值。`yield`关键字必须用在定义了至少一个`__next__()`方法的函数中，这样才能让这个函数成为一个生成器。

    '''
    f2 = lambda : (yield)
    print(f2())



