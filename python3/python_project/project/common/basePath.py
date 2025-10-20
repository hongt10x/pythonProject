# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : basePath.py
@Time    : 2024/5/30 10:42
@Author  : Echo Wang
'''

import os

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
common_path = os.path.join(rootDir, "common")
config_path = os.path.join(rootDir, "configs")
data_path = os.path.join(rootDir, "data")
lib_path = os.path.join(rootDir, "lib")
utils_path = os.path.join(rootDir, "utils")
log_path = os.path.join(rootDir, "log")

if __name__ == '__main__':
    print(rootDir)
