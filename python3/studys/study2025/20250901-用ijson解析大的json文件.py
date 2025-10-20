# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250901-用ijson解析大的json文件.py
@Time    : 2025/9/1 14:21
@Author  : Echo Wang
'''

import ijson

flag = 11
if flag == 1:
    ...

    with open("large.json", 'r') as f:
        parse = ijson.parse(f)
        # print(parse)
        # print(next(parse))
        for prefix, event, value in parse:
            # print(prefix,event,value)
            if prefix == 'company.departments.item.employees.item.name':
                print(value)

flag = 11
if flag == 1:
    ...
    with open("large2.json", "r", encoding="utf-8") as f1:
        for obj in ijson.items(f1, "users.item"):
            print(obj["name"])

flag = 11
if flag == 1:
    ...
    with open('large2.json', 'r', encoding='utf-8') as f:
        for prefix, event, value in ijson.parse(f):
            # print(prefix,event,value)
            if prefix == 'users.item.name':  # 只提取 name 字段
                print(value)

flag = 11
if flag == 1:
    ...
    with open('large.json', 'r', encoding='utf-8') as f:
        for emp in ijson.items(f, "company.departments.item.employees.item"):
            print(emp['name'])

flag = 11
if flag == 1:
    ...
    with open('large.json', 'r', encoding='utf-8') as f:
        for emp in ijson.items(f, "company"):
            print(emp, emp['name'], emp.get("name"))
flag = 11
if flag == 1:
    ...
    with open('large.json', 'r', encoding='utf-8') as f:
        for emp in ijson.items(f, "company.name"):
            print(emp)

flag = 11
if flag == 1:
    ...
    with open('large.json', 'r', encoding='utf-8') as f:
        for emp in ijson.items(f, "company.departments"):
            print(emp, type(emp))

    with open('large.json', 'r', encoding='utf-8') as f:
        for emp in ijson.items(f, "company.departments.item"):
            print(emp, type(emp))

flag = 11
if flag == 1:
    ...
    import gc

    print(gc.get_threshold())
    gc.set_threshold(1000, 10, 10)
    print(gc.get_threshold())

flag = 11
if flag == 1:
    ...
    import gc

    # 设置阈值
    # gc.set_threshold(1000, 10, 10)

    # 模拟对象分配
    objects = [object() for _ in range(1000)]  # 分配1000个对象后可能触发第0代回收

    # 检查当前阈值
    print(gc.get_threshold())  # 输出: (1000, 10, 10)

flag = 11
if flag == 1:
    ...
    with open('large3.json', 'r', encoding='utf-8') as f:
        for emp in ijson.items(f, "item.users.item"):
            print(emp, type(emp))

flag = 11
if flag == 1:
    ...
    with open('large3.json', 'r', encoding='utf-8') as f:
        for emp in ijson.items(f, "item.names"):
            print(emp, type(emp))
            for _ in emp.items():
                print(_)
