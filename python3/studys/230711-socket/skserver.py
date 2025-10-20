# -*- coding: utf-8 -*-
# time: 2023/7/11 10:40
# file: skserver.py
# author: wht

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ('127.0.0.1', 9999)
sk.bind(ip_port)
sk.listen()
print('---服务端上线---')
conn, addr = sk.accept()
print("---客户端地址---", addr)
print("---socket对象---", conn)


client_data = conn.recv(1024)
print('---接受到客户端数据---',client_data.decode('utf8'))
send_data = input('---请输入---')
conn.sendall(send_data.encode('utf8'))
conn.close()
sk.close()
