# coding: utf8
# 02-给类装配新的方法.py
# 2024/3/11

import types


class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('----%s 正在吃----' % self.name)

    @classmethod
    def swin(self):
        # print('---%s 正在游泳----' % self.name)  #实例有个name，类没有
        print('---%s 正在游泳----' % "laowang")


def run(self):
    print("---%s 正在跑----" % self.name)



if __name__ == '__main__':
    p1 = Person('王五')
    # print(p1.name)
    p1.eat()
    p1.swin()
    # 将方法run装配到实例p1上
    p1.go = types.MethodType(run, p1)
    p1.go()

    for _ in dir(p1):
        if _.startswith('_'):
            continue
        print(_)

    print('===='*4)
    for _ in dir(Person):
        if _.startswith('_'):
            continue
        print(_)

