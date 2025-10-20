# -*- coding: utf-8 -*-
# time: 2023/9/4 14:14
# file: cs_server_指定换行结尾.py
# author: wht

import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen()

while True:
    conn,addr = sk.accept()
    print(f'conn:{conn}, addr:{addr}')
    while True:
        send_data = str(input('请输入：')) + '\n'
        conn.sendall(send_data.encode('utf8'))
        client_data = conn.recv(1)
        if client_data:
            print(f'接收到的数据为：{client_data}')
        else:
            break
    conn.close()
sk.close()
