# -*- coding: utf-8 -*-
# time: 2023/7/17 14:59
# file: test02.py
# author: wht
import time

#
# print('你是有空的星星{:<6},对象{:^7},歌手世界{:>9}.'.format(999,"邓紫棋","火星人"))
#
#
#
# a = 'goodbye'
#
# print(f'good{a:0>9}')
#
# for i in range(10):
#     if i >= 5:
#         continue
#     print(i)
# else:
#     print("bye")


# for i in range(10,0,-1):
#     print(f'\r倒计时{i}秒',end='') #\r光标回到行首
#     time.sleep(1)

# print(1,3,5,7,sep='*')


import sys

# print(sys.path)

# print(sys.argv)
# for _ in sys.path:
#     print(_)

# for i in range(10):
#     if i%2 ==0:
#         print(i)
#
# print([i for i in range(10) if i%2==0])
# print([0 for i in range(10) if i%2==0])


# print(hasattr(list,'append'))

count = 0
for i in range(1000):
    if '9' in str(i):
        count += 1
print(count)
print(len([i for i in range(1000) if '9' in str(i)]))
