# -*- coding: utf-8 -*-
# time: 2023/9/12 9:43
# file: test230912.py
# author: wht


def f1(x):
    print('...f1...')
    ret = yield x*2
    print(f'...go on {ret} ...')

# f1 = f1('888')
# print(next(f1))
# print(f1.send('6666'))
# print(next(f1))

#
# print(f1('bye').send(None))
# print(next(f1(999)))
# print(next(f1('999')))

def f2(x):
    while True:
        print('..ld.f1...')
        ret = yield x*2
        if ret:

            print(f'...go on {ret} ...')

# f2 = f2('000')
# print(next(f2))
# print(f2.send('sendyou'))
# print(next(f2))


#
# def gen():
#     try:
#         print('start...')
#         yield 1
#     except ValueError:
#         yield 'ValueError'
#     finally:
#         print('finally')
#
# g = gen()   # 创建一个生成器
# print(g.__next__()) # 1
# # 向生成器内部传入异常 返回ValueError
# print(g.throw(ValueError))
# # print(g.throw(KeyError))

a = '狗殴打'
print('kk:{}'.format(a))

