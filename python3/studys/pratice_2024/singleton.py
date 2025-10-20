
# -*- coding: GBK -*-
'''
@Project ：python3 
@File    ：singleton.py
@Date    ：2024/4/15 15:06 
'''

flag = 11
if flag == 1:
    ...


    # 模块在导入时生产单例模式
    class Singleton:
        def foo(self):
            pass


    singlet = Singleton()

flag = 1
if flag == 1:
    ...


    class Goods:
        def __init__(self):
            print('__init__')

        def __new__(cls, *args, **kwargs):
            print('__new__')
            return super().__new__(cls)

        def __call__(self, *args, **kwargs):
            print('__call__')


    g = Goods()

flag = 1
if flag == 1:
    ...


    class C1:
        @classmethod
        def f(self):
            print('f')


    def f1() -> C1: ...


    print(f1(),type(f1()))
