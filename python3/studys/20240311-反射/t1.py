# coding: utf8
# t1.py
# 2024/3/11


good = 999


class T1:
    name = 'alex'

    def f1(self):
        print('--f1--')

    def f2(self):
        print('--f2--')


def dec(self):
    print('---我是doc---')


if __name__ == '__main__':
    flag = 1
    if flag == 1:
        ...

        t = T1()
        choice = input('请输入调用方法>>>:', )
        if hasattr(t, choice):
            print(getattr(t, choice))
        else:
            print('开始装配新的属性或方法')
            # setattr(t,choice,good)
            # print(getattr(t,choice))
            ...
            setattr(t, choice, dec)
            for _ in dir(t):
                if not _.startswith("_"):
                    print(_)
            # print(getattr(t,'xxx')(t))
    flag = 11
    if flag == 1:
        ...
        a1 = {list: lambda :print('xxx')}
        for i,j in a1.items():
            print(i,type(i))
            print(j,type(j))

    flag = 11
    if flag == 1:
        ...
        class T1:
            dist = 100
            def __init__(self):
                print(f'init: {self.dist}')

            def __call__(self, *args, **kwargs):
                print(f'call: {self.dist}')

            def f1(self):
                print('f1')

            def __new__(cls, *args, **kwargs):
                print(f'new: {cls.dist}')
                return super().__new__(cls)

        t = T1()
        t()

        # new: 100
        # init: 100
        # call: 100

