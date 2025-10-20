# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：01-验证解读ini文件.py
@Date    ：2024/2/27 14:05 
'''

from configparser import ConfigParser

cfg = ConfigParser()
# print(type(cfg))
cfg.read('loguru.ini',encoding='utf-8')
# cfg.read('loguru.ini',encoding='unicode-escape')


flag = 11
if flag == 1:
    ...

    print(cfg.sections())
    print(cfg.options('fod'))
    print(cfg.get('fod','fruit1'))
    print(cfg.get('fod','fruit3',fallback='找不到我吧'))
    print(cfg['fod']['fruit1'])
    # options不区分大小写
    print(cfg['fod']['FRUIT1'])
    print(cfg['1']['1'],type(cfg['1']['1']))

    print(cfg.get("log","format"))

    cfg.set('1','test', '100')
    print(cfg['1']['test'],type(cfg.get('1','test')))
    input()
    print(cfg.get('fod','FRUIT2'))
    print("=======")
    # section对字母大小写敏感， option对字母大小写不敏感
    # configparser.NoSectionError: No section: 'FOD'
    # print(cfg.get('FOD','fruit1'))

    cfg.add_section('like')

    cfg.set('like','run','9999')
    print(cfg.sections())
    print(cfg['like']['run'])

    # 必须先创建seciton，否则报错:configparser.NoSectionError: No section: 'like1'
    cfg.add_section('like1')
    cfg.set('like1','run1','99991')


    # with open('loguru1.ini','w',encoding='utf8') as fo:
    #     cfg.write(fo)

flag = 1
if flag == 1:
    ...

    print(cfg.has_section('fod'))
    print(cfg.has_option('fod','FRUIT1'))
    print(cfg.has_option('fod','fruit1'))
    print(cfg.has_option('FOD','fruit1'))
    print(cfg.has_option('fod', 'fruit4'))
    print(cfg.get('fod','fruit1'))

