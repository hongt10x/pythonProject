# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : good1.py
@Time    : 2025/5/30 16:05
@Author  : Echo Wang
'''
from good1 import Excle_G01


class G02:
    def good02(self):
        g01 = Excle_G01()
import yaml
import pprint

def get_yml_data(file_path):
    with open(file_path, encoding="utf-8") as fo:
        return yaml.safe_load(fo.read())

g02 = G02().good02()

# ret = get_yml_data(
#     r'D:\PythonStudy\python3\20240527-处理excel数据\project_os\configs\configDatas'
#     r'.yml')
# pprint.pprint(ret)