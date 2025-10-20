# # -*- coding: utf-8 -*-
# # time: 2023/8/22 16:35
# # file: 验证编码问题.py
# # author: wht
#
#
# # dic = {u'新增':999,u'删除':888}
# # print(dic.keys())
# # print(f'{dic.keys()}'ar
#
#
# # from array import array
# # from random import random
# # floats = array('d', (random() for i in range(10)))
# # # print(floats)
# # # for i,j in enumerate(floats):
# # #     print(i,j)
# # print(array['d'])
#
# import numpy as np
#
# # a = np.arange(12)
# # print(a,type(a))
# # print(a.shape)
# # a.shape = 3,4
# # print(a)
# # # print(a[2])
# # # print(a[2,1])
# # # print(a[:,1])
# #
# # # 变列排
# # print(a.transpose())
#
# # floats = np.loadtxt('requirements.txt')
# # print(floats[-1])
# # print(3*.5)
#
#
# from collections import deque
# # 双向队列
# dq = deque(range(10),maxlen=10)
# print(dq)
# dq.rotate(3)
# print(dq)
#
# # 队列的旋转操作接受一个参数 n，当 n > 0 时，队列的最右边的 n
# # 个元素会被移动到队列的左边。当 n < 0 时，最左边的 n 个元素会被
# # 移动到右边。
# dq.rotate(-4)
# print(dq)
#
# dq.append(99)
# print(dq)
#
# # 当试图对一个已满（len(d) == d.maxlen）的队列做尾部添加操作
# # 的时候，它头部的元素会被删除掉。注意在下一行里，元素 0 被删除
# # 了。
# # ❹ 在尾部添加 3 个元素的操作会挤掉 -1、1 和 2
# dq.appendleft(-1)
# print(dq)
#
# dq.extend([11,33,55])
# print(dq)
#
# dq.extendleft([22,33,44,55])
# print(dq)
#
# dq.popleft()
# print(dq)
# dq.reverse()
# print(dq)
#
# print(dq.insert(0,100))
# print(dq)
#
# # dq.clear()
# # print(dq)
#
#
#
# import bisect
# #
# # # a = [i for i in range(5)]
# a = [5,6,7,8,9]
# # print(a, type(a))
# #
# # # 而 lo 和 hi 为可选参数，分别定义查找范围/返回索引的 上限和下限，
# # # 缺省时默认对整个序列查找。
# print(bisect.bisect_left(a, 110))

import bisect

# A series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]
# values.sort(reverse=False)
# print(values)
# print(bisect.bisect_left(values, 75))
# print('New  Pos  Contents')
# print('---  ---  --------')

# l = []
# for i in values:
#     position = bisect.bisect(l, i)
#     print(f'i: {i} -- position: {position}')
#     bisect.insort(l, i)
#     print('{:3}  {:3}'.format(i, position), l)

# extra = [1,3,4]
#
# print(extra)
# print(*extra)
#
# l = [238,13,23,'88','5',100]
# b = sorted(l, key=int)
# print(b)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

# country_code = {country: code for code, country in DIAL_CODES}
# print(country_code)

# l = [3,3,4,4,5,43]
# for i,j in enumerate(l,1):
#     print(i,j)
#
#
# di = {'good':[999],'name':['往往']}
# print(di)
# key = 'good1'
#
# di.setdefault(key, []).append('800')
# print(di)
#
# from collections import defaultdict
# li = [33,4]
# dd = defaultdict(list)
# print(dd)
# dd['hh'] = 9999
# print(dd)
#
# from unicodedata import name
# print("--->",name('µ'))
#
# b={chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),"")}
# print(b)
from collections import abc

# a = [1,3,5,7]
# b = [2,4,6,8]
# print(set(a)&set(b))
#
# c = set(a)
# print(c)
#
# c.add(999)
# print(c)
#
# c.discard(31)
# print(c)
#
# c.remove(3)
# print(c)
#
# d = {'a':11,'d':99,'c':22,'b':77}
# print(d)
#
# print(d.keys())
# print(d.values())

# d1 = {sorted(k,reverse=False):v for k,v in d.items()}
# print(d1)
# data = 'hello'
# from hashlib  import md5
# m = md5()
# print(m.hexdigest())
# print(data.encode('utf8'),type(data.encode('utf8')))
# m.update(data.encode('utf8'))
# print(m.hexdigest())

a = [('key1',111),('key2',333)]
b = dict(a)

# b.__missing__ = "我看你是想整事"
# print(dir(b))

a = u'心中'
print(a.encode('u8'))

print(all(a))











