# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250711-算数.py
@Time    : 2025/7/11 11:23
@Author  : Echo Wang
'''


def is_prime(n):
    '''查看一个数是否是质数'''
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        # print(i)
    return True


def gcd(a, b):
    '''求最大公约数：greatest common divisor'''
    while b:
        print(a, b)
        a, b = b, a % b  # 相当于a,b做了交换，左大右小
        # print(a, b)
    return a

def t1(n):
    while n:
        n-=1
        print(n)


if __name__ == '__main__':
    flag = 11
    if flag == 1:
        ...
        n = 29
        print(int(n ** 0.5))
        print(is_prime(n))
        n = 37
        print(int(n ** 0.5))
        print(is_prime(n))
    flag = 1
    if flag == 1:
        ...
        print(gcd(20, 10))
        print("-" * 20)
        print(gcd(105, 1000))
        print("-" * 20)
        print(gcd(1000, 105))
        print("-" * 20)
        print(gcd(113, 79))
    flag = 11
    if flag == 1:
        ...
        t1(5)
    flag = 11
    if flag == 1:
        ...
        import math
        import inspect

        print(math.gcd(-1000, 105,15))
        # print(inspect.getsource(math.gcd))
        print(math.lcm(-1000,105))