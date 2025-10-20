# -*- coding: utf-8 -*-
# time: 2023/7/11 10:40
# file: skclient.py
# author: wht

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ('127.0.0.1', 9999)
print('---开始连接服务端---')
sk.connect(ip_port)
send_data = input('---请输入---')
sk.sendall(send_data.encode('utf8'))
server_data = sk.recv(1024)
print('---接受到服务端数据---',server_data.decode('utf8'))

sk.close()