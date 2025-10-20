# -*- coding: utf-8 -*-
import json
import threading

import requests
################################################################################
## Form generated from reading UI file 'gui页面设计.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# 1.运行qt的gui程序，创建对象
from PySide2.QtWidgets import QApplication
# 2.打开ui文件
from PySide2.QtCore import QFile
# 3.py代码需要加载ui文件
from PySide2.QtUiTools import QUiLoader


# --------------------------逻辑区-----------------------
class HttpRequest:
    def __init__(self):
        qfile = QFile('./230721_url.ui')
        qfile.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(qfile)
        qfile.close()
        self.ui.send_.clicked.connect(self.request_send)

    def convert_json(self, arg):
        if arg.strip() != "":
            return json.loads(arg)

    def request_send(self):
        method = self.ui.method_.currentText()
        url = self.ui.url_.text()
        header = self.convert_json(self.ui.header_area.toPlainText())
        print(header)

        pyload = self.convert_json(self.ui.body_area.toPlainText())

        req = requests.Request(method, url, headers=header, data=pyload)
        prepare = req.prepare()  # 获取请求前数据
        self.print_request(prepare)
        # print(prepare.body)
        s = requests.Session()  # 创建会话
        thread1 = threading.Thread(target=self.thread_func, args=(s, prepare))
        thread1.start()

    def thread_func(self, s, prepare):
        #   多线程，防止阻塞
        # 返回响应对象
        res = s.send(prepare)
        # 接受响应数据
        self.print_response(res)

    def print_request(self, req):
        MsgBody = req.body if req.body else ""
        # if req.body == None:
        #     MsgBody = ""
        # else:
        #     MsgBody = req.body
        self.ui.response_data.append(
            '{}\n{}\n{}\n{}'.format(
                '\n--------请求数据--------',
                req.method + " " + req.url,
                '\n'.join(f'{k}:{v}' for k, v in req.headers.items()),
                MsgBody
            )
        )

    def print_response(self, resp):
        resp.encoding = 'utf-8'
        self.ui.response_data.append(
            '{}\nHTTP/1.1 {}\n{}\n{}'.format(
                '\n--------响应数据--------',
                resp.status_code,
                '\n'.join(f'{k}:{v}' for k, v in resp.headers.items()),
                resp.text
            )
        )


# -------------------------------------------------


app = QApplication([])  # sys.argv  列表--创建应用程序
httpRequest = HttpRequest()
httpRequest.ui.show()
app.exec_()
