# -*- coding: utf-8 -*-
# time: 2023/7/11 14:15
# file: multiServer.py
# author: wht

import socketserver


class multiServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('---服务端上线---')
        while True:
            rdatas = self.request.recv(1024)
            print(rdatas.decode('utf8'))

            sdatas = input('请Server输入>>>')
            self.request.sendall(sdatas.encode('utf8'))
        self.request.close()


ip_port = ('127.0.0.1', 9988)
server = socketserver.ThreadingTCPServer(ip_port, multiServer)
server.serve_forever()
