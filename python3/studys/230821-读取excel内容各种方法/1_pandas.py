# -*- coding: utf-8 -*-
# time: 2023/8/21 9:53
# file: 1_pandas.py
# author: wht


import pandas as pd

# pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.notebook_repr_html', True)
# 当你将 display.notebook_repr_html 设置为 False 时，Pandas 对象会以纯文本格式显示，类似于在终端中显示的效果
# 当设置为 True（默认值）时，Pandas 对象在 Jupyter Notebook 中会以 HTML 格式渲染，通常会提供更美观、更丰富的表格显示效果
test_flag = 11
if test_flag == 1:
    wb = pd.read_excel(io=r't1.xlsx', sheet_name=None)
    # print("=" * 20)
    # print(wb,)
    # print("="*20)
    sh = wb.get("Sheet1")
    for k, v in sh.items():
        print(v)

test_flag = 11
if test_flag == 1:
    wb = pd.read_excel(io=r'test.robot.xlsx')
    print(wb)
test_flag = 11
if test_flag == 1:
    wb = pd.read_excel(io=r'test.robot.xlsx', sheet_name=1)
    print(wb)
test_flag = 11
if test_flag == 1:
    wb = pd.read_excel(io=r'test4.xls')
    print(wb, type(wb))
test_flag = 11
if test_flag == 1:
    wb = pd.read_excel(io=r'test_csv.csv')
    print(wb)

test_flag = 11
if test_flag == 1:
    wb = pd.read_excel(io=r'test.robot - header.xlsx', sheet_name=1, header=3)
    print(wb)

test_flag = 11
if test_flag == 1:
    wb = pd.read_excel(io=r'test.robot - header.xlsx', sheet_name=1, header=2)
    print(wb.dtypes)
test_flag = 11
if test_flag == 1:
    wb = pd.read_excel(io=r'test.robot - header.xlsx',
                       parse_dates=[2],
                       date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'),
                       sheet_name=1, header=1)
    print(wb)

test_flag = 11
if test_flag == 1:
    with open(r'D:\PythonStudy\python3\230821-excel\text.txt', 'rb') as fd:
        _line = fd.read()
        line = fd.readline()
        lines = fd.readlines()
        print(_line, '\n', type(_line))
        print(line, '\n', type(line))
        print(lines, '\n', type(lines))
        kk = (k for k in lines)
        print(kk, '\n', type(kk))

test_flag = 1
if test_flag == 1:
    fd = pd.read_csv('t3.csv', encoding='utf8', sep=',')
    print(fd)
