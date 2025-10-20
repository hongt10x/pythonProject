# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250902-读取大文件策略.py
@Time    : 2025/9/2 10:44
@Author  : Echo Wang
'''

flag = 11
if flag == 1:
    ...
    chunk_size = 12 * 12
    with open("example2.txt", "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            # process(chunk)
            print("*"*30)
            print(chunk)

flag = 11
if flag == 1:
    ...
    with open("large.json", "r", encoding="utf-8") as f:
        for line in f:
            print(line)

flag = 11
if flag == 1:
    ...
    with open("large.json", "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print("*"*30)
            print(line,end="")

flag = 11
if flag == 1:
    ...
    with open("large.json", "r", encoding="utf-8") as f:
        line = f.readline()
        while line:
            line = f.readline()
            print(line, end="")
