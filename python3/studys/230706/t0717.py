# -*- coding: utf-8 -*-
# time: 2023/7/17 16:42
# file: t0717.py
# author: wht

import yaml

# with open('1.yml', encoding='UTF8') as f:
#     text = yaml.load(f,Loader=yaml.FullLoader)
#     print(text)
#
# with open('2.yaml', encoding='UTF8') as f:
#     text = yaml.load(f,Loader=yaml.FullLoader)
#     print(text)
#
# with open('2.yaml') as f:
#     text = yaml.load(f,Loader=yaml.FullLoader)
#     print(text)

with open('3.yml', encoding='UTF8') as f:
    text = yaml.load_all(f,Loader=yaml.FullLoader)
    for one in text:
        print(one)

# with open('4.yml', encoding='UTF-8') as f:
#     text = yaml.load(f,Loader=yaml.FullLoader)
#     print(text)

# with open('1.yml',encoding='utf8') as f:
#     text = yaml.safe_load_all(f)
#     for i in text:
#         print(i)
#
with open('1.yml',encoding='utf8') as f:
    text = yaml.load(f.read(),Loader=yaml.BaseLoader)
    print(text)





