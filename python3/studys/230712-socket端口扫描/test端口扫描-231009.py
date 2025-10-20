# -*- coding: utf-8 -*-
# time: 2023/7/12 9:54
# file: test端口扫描.py
# author: wht

import socket
import re
import threading
from asyncio import sleep


def scan_port(port):
    # ip = input('请输入ip >>>')
    # ip = '42.192.62.8'
    # ip = '127.0.0.1'
    ip = '110.242.68.66'
    # ports = input('请输入ports范围:0-65535 >>>')
    # port_start, port_end = ports.split('-')
    # for port in range(int(port_start), int(port_end) + 1):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sk.settimeout(0.5)
    # print('port:',port)
    conn = sk.connect_ex((ip, port))
    # print('conn:',conn)
    try:
        if conn == 0:
            print(f'主机：{ip}，端口：{port}已开放')
    except:
        pass
    sk.close()


for port in range(30000,65535,4):
    # sleep(0.5)
    t1 = .Thrthreadingead(target=scan_port, args=(port,))
    t2 = threading.Thread(target=scan_port, args=(port+1,))
    t3 = threading.Thread(target=scan_port, args=(port+2,))
    t4 = threading.Thread(target=scan_port, args=(port+3,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()




