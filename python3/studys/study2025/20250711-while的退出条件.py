# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250711-while的退出条件.py
@Time    : 2025/7/11 15:03
@Author  : Echo Wang
'''

'''
    在 Python 中，while 循环的退出条件是当循环条件表达式的值为 False、None、0、""（空字符串）、[]（空列表）、{}（空字典）等“假值”（Falsy）时，循环就会退出。以下是详细的分类和示例：
    
    1. 常见的“假值”（Falsy）条件
    当 while 后面的条件是以下值时，循环会退出：
    
    False
    None
    数值 0 或 0.0
    空字符串 ""、''
    空序列或集合：
    空列表 []
    空元组 ()
    空字典 {}
    空集合 set()
    其他假值：
    自定义类的实例如果实现了 __bool__() 或 __len__() 方法并返回 False 或 0。
     复数 0j 也为假
    除了条件变为“假值”，还可以通过以下方式退出 while 循环：
    break, return, try...exception异常捕获
    
    
    总结：
    while 循环的退出条件包括：
    条件表达式的结果是“假值”（Falsy）：
    False
    None
    0、0.0、0j
    ""、[]、()、{}、set()
    自定义对象如果 __bool__() 返回 False 或 __len__() 返回 0。
    通过 break、return 或异常强制退出。
    修改控制变量，使条件表达式最终变为假值。
'''

print("test")
# 条件为 False
while False:
    print("不会执行")

# 条件为 None
while None:
    print("不会执行")

# 条件为 0
while 0:
    print("不会执行")

# 条件为空字符串
while "":
    print("不会执行")

# 条件为空列表
while []:
    print("不会执行")

while 0j:
    print("不会执行")

_iterator = [1, 3, 5].__iter__()
try:
    while True:
        data = next(_iterator)  # 如果迭代器耗尽，会抛出 StopIteration
        print(data)
except StopIteration:
    pass  # 循环退出
