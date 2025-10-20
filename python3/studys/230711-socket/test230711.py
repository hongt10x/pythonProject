# # -*- coding: utf-8 -*-
# # time: 2023/7/11 15:25
# # file: test230711.py
# # author: wht
#
# import re
# def check_ip(ip):
#     # ip_patten = re.compile('(^((2[0-4]\d.)|(25[0-5].)|(1\d{2}.)|(\d{1,2}.))((2[0-5]{2}.)|(1\d{2}.)|(\d{1,2}.){2})((1\d{2})|(2[0-5]{2})|(\d{1,2})))')
#     ip_patten = re.compile(r'(?<![\.\d])(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?![\.\d])')
#     if ip_patten.match(ip):
#         return True
#     else:
#         return False
#
#
# print(check_ip('299.0.0.1'))
from time import sleep
import threading

def doing():
    while True:
        print('我在做事情...\n')
        sleep(1)


t1 = threading.Thread(target=doing)
t2 = threading.Thread(target=doing)
# t1.setDaemon(t1)
t1.setDaemon(True)
# t1.setDaemon(t1)
t2.setDaemon(True)

t1.start()
t2.start()
# t1.join()
# t2.join()
for i in range(10):
    sleep(1)
    print('主线程结束...')


