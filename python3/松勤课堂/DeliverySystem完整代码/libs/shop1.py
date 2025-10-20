# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：shop1.py
@Date    ：2024/2/29 17:35 
'''

from common.baseApi import BaseAPI
from libs.login import Login
import jsonpath
class Shop(BaseAPI):
    pass



if __name__ == '__main__':
    login_data = {'username': 'yp0731', 'password': '17805'}
    token = Login().login(login_data, get_token=True)

    # print("token:",token)
    shop = Shop(token)
    query_data = {'page':1,'limit':20}

    # shop.query(params=query_data)
    res = shop.query(query_data)
    print(res)
    print(jsonpath.jsonpath(res, '$.data.records[0].id'))
