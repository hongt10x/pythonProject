# -*- coding: utf-8 -*-
# time: 2023/9/4 14:14
# file: cs_client_指定换行结尾.py
# author: wht

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ('127.0.0.1',9999)
sk.connect(ip_port)
while True:
    send_data = str(input('输入:')) + '\n'
    # send_data = str(input('输入:'))
    sk.sendall(send_data.encode('utf8'))
    server_data = sk.recv(1)
    if server_data:
        print(f'接收服务端信息：{server_data.decode("utf8")}')
    else:
        break
sk.close()