# # -*- coding: utf-8 -*-
# # time: 2023/11/24 16:25
# # file: -map-reduce-zip.py
# # author: wht
#
# # flag = 1
# # if flag == 1:
# #     pass
# def fun(x):
#     return x * 2
#
#
# list1 = [1, 2, 3, 45]
#
# list2 = map(fun, list1)
# # print(list(list2))
# list3 = map(lambda x: str(x), list1)
#
#
# # list4 = list(list3)
# # print(list4)
# # print("::".join(list4))
#
#
# def f1(x, y):
#     print("x={},y={}".format(x, y))
#     print(x * y)
#     return x * y
#
#
# from functools import reduce
#
# l1 = [1, 3, 2, 5, 6]
# print(reduce(f1,l1))
# print(reduce(f1,l1,100100))
#
# l3 = [3, 4, 5, 6, 6]
# # l2 = reduce(f1, l1, 100)
# # print(l2)
# # l4 = reduce(f1, l1, l3)
# # print(l4)
#
# from functools import reduce
#
# scientists = ({'name': 'Alan Turing', 'age': 105, 'gender': 'male'},
#               {'name': 'Dennis Ritchie', 'age': 76, 'gender': 'male'},
#               {'name': 'Ada Lovelace', 'age': 202, 'gender': 'female'},
#               {'name': 'Frances E. Allen', 'age': 84, 'gender': 'female'})
#
#
# def reducer(accumulator, value):
#     print("accumulator={},value={}".format(accumulator, value))
#     sum = accumulator + value['age']
#     # print(sum)
#     return sum
#
#
# total_age = reduce(reducer, scientists, 0)
# print(total_age)
#
#
# def group_by_gender(accumulator, value):
#     print("accumulator={},value={}".format(accumulator, value))
#     accumulator[value['gender']].append(value['name'])
#     return accumulator
#
#
# #
# grouped = reduce(group_by_gender, scientists, {'male': [], 'female': []})
# print(grouped)
#
#
# def f2(x):
#     if x > 0:
#         return x
#
#
# alist1 = [-1, 0, 3, 2, 4, 3, 8, ]
#
#
# # print(list(filter(f2, alist1)))
#
#
# def f3(x):
#     if x % 2 == 0:
#         print(x)
#         return x
#
#
# print(list(filter(f3, alist1)))
#
# # 在某些情况下，我们可能希望直接使用filter()函数来过滤掉可迭代对象中的一些"假值"，例如空字符串、零等。此时，可以将filter()
# # 的函数参数设置为None，filter()函数会自动过滤掉那些判断为假的元素
# a1 = [1, "", 0, "C", None, {}, False, 3.14, {"x": 9}, ' ', (), [], "abc"]
# print(list(filter(None, a1)))
#
# a2 = [1, 3, 4, 5]
#
#
# def good1(x, y):
#     print(x, y)
#     return x + y
# # 初始值默认为None，如果存在则将其放在序列中元素计算之前，并且在序列为空值作为默认值
# print(reduce(good1, a2))
# print(reduce(good1, a2,100))


l1 = [1,3,5,7]
l2 = [2,4,6,8]

# f = lambda x,y:x*y
# print(list(map(f, l1, l2)))
# f1 = lambda x:x**2
#
# print(list(map(f1,l1,)))

from functools import reduce
f2 = lambda x,y:x+y
# print(reduce(f2,l1,100))

l3 = [l1,l2]
print(reduce(f2,l3,))


# print(reduce(f2,l1,))
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# 创建一个空列表来存储结果
result = []

# 使用zip()函数同时迭代两个列表
for x, y in zip(list1, list2):
    # 对每对元素进行操作，这里是简单的相加操作
    sum_value = x + y
    # 将结果添加到结果列表中
    result.append(sum_value)

# 打印结果
print(result)