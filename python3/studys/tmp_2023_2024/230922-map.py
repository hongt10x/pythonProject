# -*- coding: utf-8 -*-
# time: 2023/9/22 10:34
# file: 230922-map.py
# author: wht

from time import sleep, strftime
from concurrent import futures
def display(*args): #➊
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)
def loiter(n): #➋
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10 #➌
def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3) #➍
    results = executor.map(loiter, range(5)) #➎
    display('results:', results) #➏
    display('Waiting for individual results:')
    for i, result in enumerate(results):# ➐
        display('result {}: {}'.format(i, result))

main()



# s = 'wang'
# u = s.encode('utf8')
# print(u,type(u))
#
# uu = u'good'
# ss = uu.encode('utf8')
# print(ss,type(ss))
#
# sss = ss.decode('unicode_escape')
# print(sss,type(sss))







