# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：t1-函数和方法区别.py
@Date    ：2024/1/29 10:08 
'''
import pprint

import beeprint


class Person:
    King = 'wang'


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    @classmethod
    def good_info(cls):
        print('goodinfo..')

    @staticmethod
    def static_good_info():
        print('static_good_info')

    def goodbye():
        print("goodbye")

if __name__ == '__main__':
    import inspect
    # beeprint.pp(inspect.getmembers(Person))
    # pprint.pp(inspect.getmembers(Person))
    # print('\n')
    # pprint.pprint(inspect.getmembers(Person))


    # def is_sting(x):
    #     '''内容说明
    #         1、只输出字符串对象
    #     '''
    #     if isinstance(x,str):
    #         return True
    #     else:
    #         return False
    #
    # pprint.pp(inspect.getmembers(Person,is_sting))
    pprint.pp(inspect.getmembers(Person,lambda x: True if inspect.isclass(x) else False))
    pprint.pp(inspect.getmembers(Person,lambda x: True if inspect.ismethod(x) else False))
    pprint.pp(inspect.getmembers(Person,lambda x: True if inspect.isfunction(x) else False))
    # pprint.pp(inspect.getmembers(Person))
    # pprint.pp(inspect.getmembers(Person('WANG',22)))