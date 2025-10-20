# coding: utf8
# path.py
# 2023/6/2

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASEDIR)
config_path = os.path.join(BASEDIR, 'configs')
utils_path = os.path.join(BASEDIR, 'utils')
data_path = os.path.join(BASEDIR, 'data')


if __name__ == '__main__':
    print(utils_path)
