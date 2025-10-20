# -*- coding: utf-8 -*-
# time: 2023/7/12 9:54
# file: test端口扫描.py
# author: wht

import socket
import re


def scan_port():
    # ip = input('请输入ip >>>')
    # ip = '42.192.62.8'
    ip = '110.242.68.66'
    ports = input('请输入ports范围:0-65535 >>>')
    port_start, port_end = ports.split('-')
    for port in range(int(port_start), int(port_end) + 1):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(0.5)
        # print('port:',port)
        conn = sk.connect_ex((ip, port))
        # print('conn:',conn)
        try:
            if conn == 0:
                print(f'主机：{ip}，端口：{port}已开放')
        except:
            pass
        sk.close()


def check_ip(ip):
    # ip_patten = re.compile('(^((2[0-4]\d.)|(25[0-5].)|(1\d{2}.)|(\d{1,2}.))((2[0-5]{2}.)|(1\d{2}.)|(\d{1,2}.){2})((1\d{2})|(2[0-5]{2})|(\d{1,2})))')
    ip_patten = re.compile(
        r'(?<![\.\d])(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?![\.\d])')
    if ip_patten.match(ip):
        return True
    else:
        return False


if __name__ == '__main__':
    scan_port()
