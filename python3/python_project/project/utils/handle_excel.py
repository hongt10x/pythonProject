# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : handle_excel.py
@Time    : 2024/5/30 10:47
@Author  : Echo Wang
'''

from openpyxl import load_workbook


def get_excel_data(file_path):
    return load_workbook(file_path, data_only=True)
