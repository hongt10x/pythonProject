# -*- coding: utf-8 -*-
# time: 2023/7/26 16:25
# file: test230726.py
# author: wht
'''
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('loguru.ini', encoding='utf8')
print(cfg.sections())
print(cfg.options(cfg.sections()[1]))
print(cfg.has_section('log'))
if cfg.has_option('log', 'level'):
    print(cfg.get('log', 'level'))
if cfg.has_option('fod', 'fruit1'):
    print(cfg.get('fod', 'fruit1'))

# 增加配置数据
# cfg.add_section('hulman')
# cfg.set('hulman', 'man', '999')
print(cfg.sections())


# with open('loguru.ini', 'w', encoding='utf8') as f:
#     cfg.write(f)


def fuc(): ...

'''
#
a = '中国'
# # print(a, type(a))
# b = a.encode('utf8')
# print(b, type(b))
# # c = b.decode('unicode-escape')
# # print(c, type(c))
# # d = b.decode('utf8')
# # print(d, type(d))
#
# aa = '中国人-'
# a1 =aa.encode('gbk')
# print(a1,type(a1))
#
print(a,type(a))
b1 =a.encode('unicode-escape')
print(b1,type(b1))
# 用什么编码就用什么解码，就能得到原始数据
c = b1.decode('unicode-escape')
print(c,type(c))
#
listA = ['zhangsan', 'lisi', 'wangwu','longshenhou','lisi']
listB = ['zhangsan', 'lisi', 'zhaoliu']
#
# 交集
print(set(listA) & set(listB))
# 并集
print(set(listA) | set(listB))
# 差集
print(set(listA) - set(listB))
# 对称差集
print(set(listA) ^ set(listB))


print("**"*39)

# 交集
print(set(listA).intersection(set(listB)))
# 并集
print(set(listA).union(set(listB)))
# 差集
print(set(listA).difference(set(listB)))
# 对称差集
print(set(listA).symmetric_difference(set(listB)))

# a1 = {[1, 3]: '234'}
# print(a1, type(a1))



# a = u'中国'
# print(a,type(a))




if __name__ == '__main__':
    ...

