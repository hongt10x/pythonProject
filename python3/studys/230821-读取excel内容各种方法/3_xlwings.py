# -*- coding: utf-8 -*-
# time: 2023/8/22 14:30
# file: 3_xlwings.py
# author: wht


import xlwings as xw

app = xw.App(visible=True, add_book=False)
test_flag = 11
if test_flag == 11:
    ...
    # wb = app.books.add()
    wb = xw.Book()
    wb.display_alerts = False
    wb.screen_updating = False

test_flag = 11
if test_flag == 1:
    ...
    books = xw.books
    books = app.books

test_flag = 11
if test_flag == 1:
    ...
    wb = app.books.open(r'D:\PythonStudy\python3\230821-excel\test1.xlsx')
    wb = xw.Book('test.robot.xlsx')



