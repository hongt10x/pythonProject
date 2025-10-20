# -*- coding: utf-8 -*-
# time: 2023/7/28 17:30
# file: test230727.py
# author: wht

class A: ...


class B(A):
    def __init__(self):
        print('A......')


class C(A): ...


class D(B): ...


class F(C): ...


class G(D):
    def __init__(self):
        super().__init__(self)


class H(D): ...


if __name__ == '__main__':
    # print(G.__base__.mro())
    # for i in F.mro():
    #     print(i.__name__)

    # d = D()
    print('\033[0;30;43m显示颜色\033[0m')
