# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：06_并发锁问题.py
@Date    ：2024/4/15 16:25 
'''

import threading
import time

# from threading import Lock as lock
flag = 11
if flag == 1:
    ...

    def job1():
        global n,lock
        lock.acquire()
        for i in range(10):
            n+=1
            print(f'job1: {n}',n)
        lock.release()

    def job2():
        global n,lock
        lock.acquire()
        for i in range(10):
            n+=100
            print(f'job2: {n}',n)
        lock.release()

    n=0
    lock = threading.Lock()
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()

flag = 11
if flag == 1:
    ...
    def job1():
        global n
        with lock:
            for i in range(10):
                n+=1
                print(f'job1: {n}')

    def job2():
        global n
        with lock:
            for i in range(10):
                n += 100
                print(f'job2: {n}')

    n=0
    lock = threading.Lock()
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()


flag = 1
if flag == 1:
    ...


    def main():
        n = 0
        # 生成可重入锁对象,可重入锁（RLock），只在同一线程里放松对锁(通行证)的获取，意思是，只要在同一线程里，程序就当你是同一个人，这个锁就可以复用，其他的话与Lock并无区别
        lock = threading.RLock()
        with lock:
            for i in range(10):
                n += 1
                time.sleep(0.5)
                with lock:
                    print(n)


    t1 = threading.Thread(target=main)
    t1.start()