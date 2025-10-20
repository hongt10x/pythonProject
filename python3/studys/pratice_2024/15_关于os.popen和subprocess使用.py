# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 15_关于os.popen和subprocess使用.py
@Time    : 2024/5/26 13:08
@Author  : Echo Wang
'''

flag = 1
if flag == 1:
    ...

    import os

    cmd='hostame'
    r1 = os.popen(cmd)
    print(r1,r1.read())
    '''doc:内容说明
       1、os.popen缺陷：如果脚本报错，函数捕获不到
       2、 能获取返回值
    '''
    cmd='1.sh'
    r1 = os.popen(cmd)
    print(r1,r1.read(),r1.readline())

flag = 1
if flag == 1:
    ...
    '''doc:内容说明
       1、可以正常捕获错误返回值信息
       2、 
    '''
    import subprocess
    cmd='hostname'
    r2 = subprocess.call(cmd)

    r3 = subprocess.check_call(cmd)

    subprocess.getstatusoutput(cmd)



