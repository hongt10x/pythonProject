# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：10_高阶函数map,reduce等学习.py
@Date    ：2024/4/23 14:33 
'''

flag = 1
if flag == 1:
    ...

    # 输出格式化
    a = '77'
    # 输出字符串变量，左对齐，长度为3，不足补0
    print(f'--{a:Y<3}--')
    print(f'--{a:X>5}--')

flag = 11
if flag == 1:
    ...

    l1 = [1,3,4,6]
    f1 = lambda x:x*2
    r = map(f1,l1)
    print(list(r))



flag = 11
if flag == 1:
    ...
    # 描述：reduce方法，顾名思义就是减少，假设你有一个由数字组成的可迭代对象，并希望将其缩减为单个值。把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

    l1 = [1, 3, 4, 6]
    f1 = lambda x,y: x * y
    from functools import reduce
    r = reduce(f1,l1)
    print(r)

flag = 11
if flag == 1:
    ...
    l1 = [1, 3, 4, 6]
    f1 = lambda x: True if x>3 else False
    r = filter(f1,l1)
    print(list(r))

flag = 11
if flag == 1:
    ...
    '只要lambda的返回值是0和False，则是无效匹配；否则其他值都能有效过滤'
    l1 = [1, 3, 4, 6]
    # f1 = lambda x: False if x > 3 else False
    f1 = lambda x: 0 if x > 3 else False
    print(f1(4))
    r = filter(f1, l1)
    print(list(r))

flag = 1
if flag == 1:
    ...
    '''sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作；list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。'''
    l1 = [1, 3, 4, 6]
    print(sorted(l1))
    print(sorted(l1,reverse=True))
