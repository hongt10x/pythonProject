# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：05-反射学习.py
@Date    ：2024/4/25 17:37 
'''


flag = 1
if flag == 1:
    ...

    class WebSite:
        cut = 100
        def register(self):
            print("欢迎来到注册页面")

        def login(self):
            print("欢迎来到登录页面")

        def home(self):
            print("欢迎进入主页")
            # return

        def about(self):
            print("关于我们")

        def error(self):
            print("404 No Found!")


    from typing import Callable
    web = WebSite()

    print(type(format))
    add  = lambda a,b: a+b
    print(type(add))
    # choice = input("请输入要执行的方法>>> ")
    # if hasattr(web, choice):
    #     print(getattr(web, choice) is )
    print("="*20)
    # print(callable(getattr(web, 'cut')))
    f = getattr(web, 'home')
    # f = web.cut
    # 判断是不是可回调函数
    print(isinstance(f,Callable))
    print(isinstance(add,Callable))
    print(isinstance(format,Callable))
    print(isinstance(format,Callable))


    #  判断是不是函数，方法
    #  inspect.isfunction检查对象是否是一个用户定义的函数（即通过 def 或 lambda 创建的函数），但不包括类方法、实例方法或内置函数。
    from inspect import isfunction,ismethod
    print()
    print(isfunction(f))
    print(isfunction(add))
    #  检查对象是否是一个绑定方法（bound method），即类中定义的实例方法或类方法，并且已经绑定到某个对象（实例或类）。
    print(ismethod(f))
    print(ismethod(add))

    # print(f.__code__.co_code)
    #
    # print(dir(f.__code__))
    # print(f.__code__.co_filename)

flag = 1
if flag == 1:
    ...


