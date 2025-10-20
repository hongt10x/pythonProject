# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : pandas由浅入深应用.py
@Time    : 2025/7/28 16:16
@Author  : Echo Wang
'''

import pandas as pd

flag = 11
if flag == 1:
    ...

    # 从字典创建
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "London", "Tokyo"]
    }

    df = pd.DataFrame(data)
    print(df)

flag = 11
if flag == 1:
    ...
    f1 = pd.read_excel("test.xlsx", sheet_name="Sheet2", header=0)  # 指定第一行为首行
    # print(f1.head())  # 查看前5行
    f2 = pd.read_excel("test.xlsx", sheet_name="Sheet1", header=1)  # 指定第二行为首行
    # print(f2.tail())  # 查看后5行

    # print(f1["name"])
    # print(f2.head())
    print(f1.columns, f1.columns.nlevels)
    # subset = f2["wht1"]
    # Index(['wht1', 22, 1], dtype='object')  如果首行值为数字，那么就用数字作为键，不要写成字符串
    # print(subset)
    # print(f2[22]
    # print(f1[["name","age ","garden"]])
    print(f1["age "] > 30)  # 筛选是否大于30
    print(f1[f1["age "] > 30])  # 筛选出大于30的值
    print(list(filter(lambda x: x, f1["age "] > 30)))
    print(f1[(f1["age "] > 30) & (f1["name"] == "wht23")])  # 筛选出大于30且为wht23的行

flag = 11
if flag == 1:
    ...
    # f2 = pd.read_excel("test.xlsx", sheet_name="Sheet2", header=1)  # 指定第二行为首行
    f2 = pd.read_excel("test.xlsx", sheet_name="Sheet2", header=0)  # 指定第二行为首行


    # print(f2.info)
    # f2.dropna()
    # print(f2.info)
    # f2.fillna(0)
    # print(f2.tail())
    def capitalize_name(name: str):
        return name.capitalize()


    # print(f2["name"])
    # f2["name"] = f2["name"].apply(capitalize_name)
    # print(f2["name"])

    # f2["age"] = f2["age"].apply(lambda x:x*2)
    # print(f2["age"],type(f2["age"]))
    # print(f2.describe())
    # print(f2["age"].mean())
    # print(f2["age"].sum())
    # print(f2["garden"].mean())
    # print(f2["city"].info)

    group = f2.groupby("city")["age"].mean()
    print(group)
flag = 11
if flag == 1:
    ...
    sh3 = pd.read_excel("test.xlsx", sheet_name="Sheet3")
    # print(sh3["Age"].describe())
    print(sh3.groupby("City")["Age"].mean())

flag = 11
if flag == 1:
    ...
    import sys

    s = sys.argv
    print(s, type(s))
    c = s[1:]
    print(c[0])
    for i in c[0].split(","):
        print(i)

flag = 11
if flag == 1:
    ...
    contents = ["ip1,ip2,", "ip3"]
    ips = "".join(content for content in contents)
    print(ips)

flag = 11
if flag == 1:
    ...
    df_a = pd.read_excel(io="test.xlsx", sheet_name="Sheet1", usecols=[0])
    df_b = pd.read_excel(io="test2.xlsx", sheet_name="Sheet1", usecols=[0])
    # print(df_a.iloc[:,0],type(df_a.iloc[:,0]))

    b_values = set(df_b.iloc[:, 0])
    df_a['in_b'] = df_a.iloc[:, 0].isin(b_values)
    print(df_a[df_a["in_b"]])
    matched_rows = df_a[df_a['in_b']].index.tolist()
    print(matched_rows)

flag = 11
if flag == 1:
    ...
    a = [1, 3, 5, 6, 0]
    b = []
    print(any(a))
    print(any(b))
    print(all(a))

    print(eval("1+1"))
    print("1+1")
    print(divmod(3, 3))
    # print(divmod(3,0))

flag = 11
if flag == 1:
    ...
    from typing import Union, Sequence, Callable, Optional


    def t1(x: Union[str, int, list, dict, tuple, None] = 0):
        print(f"x:{x}")


    t1(1)
    t1([])

flag = 11
if flag == 1:
    ...


    def tes1(x: str = "www"):
        print(x)


    tes1(1)
    tes1()
    print(bin(10))
    print(hex(10))
flag = 11
if flag == 1:
    ...
    import sys


    def calculate(a, b):
        result = a + b
        sys.breakpointhook()  # 程序执行到这里会暂停，进入调试模式
        return result


    print(calculate(2, 3))

flag = 11
if flag == 1:
    ...


    @property
    def t1():
        print('xx')


    print(callable(t1))

flag = 11
if flag == 1:
    ...


    class T:
        name = "wht"
        age = "33"

        def t1(self):
            print("t1")

        def t2(self):
            print("t2")


    # for i in dir(T):
    #     if not i.startswith("__"):
    #         print(i)
    #
    # delattr(T, "name")
    # print("-"*30)
    #
    # for i in dir(T):
    #     if not i.startswith("__"):
    #         print(i)

    t = T()
    # for i in dir(t):
    #     if not i.startswith("__"):
    #         print(i)
    # print("#"*30)
    # delattr(t,"t1")
    # for i in dir(t):
    #     if not i.startswith("__"):
    #         print(i)
    # print(T.__dict__)
    print(vars(T))
    # t.sex = "male"
    # print(vars(t))
    # print(t.__dict__)
    # import inspect
    # for j in inspect.getmembers(t):
    #     print(j)

flag = 11
if flag == 1:
    ...


    # 如果类定义了 __slots__，实例没有 __dict__
    class SlottedClass:
        __slots__ = ['slot_var']

        def __init__(self):
            self.slot_var = "槽变量"


    obj = SlottedClass()
    # print(obj.__dict__)  # AttributeError: 'SlottedClass' object has no attribute '__dict__'

    print(SlottedClass.__slots__)

flag = 1
if flag == 1:
    ...
    # my_list = [0, 1, 2, 3, 4, 5]
    #
    # s1 = slice(-3, None)  # 相当于 [-3:]
    # s2 = slice(None, -2)  # 相当于 [:-2]
    # s3 = slice(None, None, -1)  # 相当于 [::-1]（反转）
    #
    # print(my_list[s1])  # [3, 4, 5]
    # print(my_list[s2])  # [0, 1, 2, 3]
    # print(my_list[s3])  # [5, 4, 3, 2, 1, 0]

    a = (x for x in range(100))
    print(a)
