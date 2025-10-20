# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : loginPage.py
@Time    : 2025/7/8 14:12
@Author  : Echo Wang
'''

from pageObjs.loginPage import LoginPage
from configs.env import Env
def loginPage():
    testlogin = LoginPage().open_test_url(Env.HOST)


if __name__ == '__main__':
    loginPage()

