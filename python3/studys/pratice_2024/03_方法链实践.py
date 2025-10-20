# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：03_方法链实践.py
@Date    ：2024/4/12 15:02 
'''

flag = 1
if flag == 1:
    ...

    class T1:
        @property
        def f1(self):
            print('f1')
            return self
        @property
        def f2(self):
            print('f2')
            return self

    t = T1()
    # t.f1
    t.f1.f2
    print('-'*20)
    t.f2.f1