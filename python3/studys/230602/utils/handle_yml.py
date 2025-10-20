# coding: utf8
# handle_yml_data.py
# 2023/6/2

import yaml


def get_yml_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        return yaml.safe_load(f.read())


if __name__ == '__main__':
    res = get_yml_data('../config/excel_config.yml')
    print(res,type(res))
