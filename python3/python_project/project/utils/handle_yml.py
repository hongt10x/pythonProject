# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : handle_yml.py
@Time    : 2024/5/30 10:46
@Author  : Echo Wang
'''

import yaml


def get_yml_data(file_path):
    with open(file_path, encoding="utf-8") as fo:
        return yaml.safe_load(fo.read())
