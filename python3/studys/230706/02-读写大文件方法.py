# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 02-读写大文件方法.py
@Time    : 2025/1/22 14:29
@Author  : Echo Wang
'''
import sys


def read_large_file(file_path, chunk_size=1024 * 8):
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data


# file_path = 'large_file.txt'
# with open("new_large_file.txt", 'wb') as fo:
#     for chunk in read_large_file(file_path):
#         fo.write(chunk)

def read_test():
    i = 0
    while True:
        i += 1
        print("read_test: ", i)
        if i > 10:
            break
        yield i


# rt = read_test()
# print(rt,type(rt))
#
# for j in rt:
#     print(j)


# t1 = (x*x for x in range(10))
# print(t1,type(t1))
# for k in t1:
#     print(k)

def p1():
    while True:
        print("p1...")
        # yield

'''多进程方法'''
from multiprocessing import pool
import sys
try:
    with pool.Pool(processes=2) as pool:

        for _ in range(2):
            pool.apply(p1,)

        pool.close()
        pool.join()
        print("join...")
    print("end...")
except Exception as e:
    sys.exit(e)

