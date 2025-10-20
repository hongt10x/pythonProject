# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：conftest.py
@Date    ：2024/2/29 13:55 
'''
import pytest
from libs.login import  Login
from configs.conf import NAME_PWD
from libs.shop import Shop
@pytest.fixture(scope='session',autouse=True)
def start_running():
    print('测试代码。。。')

@pytest.fixture(scope='session')
def login_init():
    token = Login().login(NAME_PWD,get_token=True)
    print('token:',token)
    yield token
    print("---退出----")

@pytest.fixture(scope='session')
def shop_init(login_init):
    print('--执行店铺操作')
    shop = Shop(login_init)
    yield shop