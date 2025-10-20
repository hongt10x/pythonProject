# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：02_namedtuple学习.py
@Date    ：2024/4/12 14:50 
'''

from collections import namedtuple
flag = 11
if flag == 1:
    ...

    Color = namedtuple("Color", "r g b alpha")

    def convert_string_to_color(desc: str, alpha: float = 0.0):
        if desc == "green":
            return Color(r=50, g=205, b=50, alpha=alpha)
        elif desc == "blue":
            return Color(r=50, g=0, b=255, alpha=alpha)
        else:
            return Color(r=50, g=0, b=0, alpha=alpha)


    c = convert_string_to_color('green',0.4)
    print(c,c.alpha,c.r,c.g,c.b)


flag = 1
if flag == 1:
    ...
    from typing import NamedTuple
    class Goods(NamedTuple):
        name: str = ''
        age: int =0
        def fly(self):
            print('i can fly')

    class Goods1:
        name: str = ''
        age: int =0
        def fly(self):
            print('i can fly...')


    g = Goods()
    print(type(g),g,g.fly())
    print(g.age)
    # AttributeError: can't set attribute,具名元组不可变；如果你试图改变一个namedtuple 对象的属性值，你就试图修改一个不可变的对象
    # g.age = 100
    # print(g.age)
    g1 = Goods1()
    print(type(g1),g1,g1.fly())
    print(g1.age)
    g1.age = 100
    print(g1.age)


'''内容说明
    1、
    2、
'''