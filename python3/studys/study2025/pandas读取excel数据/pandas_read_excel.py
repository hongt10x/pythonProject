# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : pandas_read_excel.py
@Time    : 2025/7/28 16:02
@Author  : Echo Wang
'''

import pandas as pd

flag = 1
if flag == 1:
    ...

    f1 = pd.read_excel("test.xlsx", sheet_name="Sheet1")
    f2 = pd.read_excel("test.xlsx", sheet_name="Sheet2")

    print([x for x in f1["name"]])
    print([x for x in f2["name"]])

    name_set = set(f1["name"].dropna().astype(str))
    print(name_set)

    f2["是否重复"] = f2["name"].apply(lambda x: x in name_set)
    with pd.ExcelWriter("output.xlsx") as writer:
        f2.to_excel(writer, sheet_name="比对结果", index=False)


flag = 1
if flag == 1:
    ...
    a = "anMe"
    print(a.capitalize())
