# -*- coding: utf-8 -*-
# time: 2023/8/19 9:51
# file: 0819mock.py
# author: wht
import requests
import time
import threading

HOST = 'http://127.0.0.1:9999'

# url = f'{HOST}/xintian_sq'
# ret = requests.request(method='GET', url=url)
# print(ret.text)
#
# url = f'{HOST}/sq'
# data = {"key1": "abc", "key2": "123"}
# ret = requests.request(method='POST', url=url, params=data)
# print(ret.text)
# print(ret.status_code)
#
#
# url = f'{HOST}/sq2'
# data = {"key1":"abc"}
# ret = requests.request(method='GET', url=url, data=data)
# print(ret.text)


# url = f'{HOST}/sq3'
# data = {"key1":"value1","key2":"value2"}
# ret = requests.request(method='POST', url=url, json=data)
# print(ret.text)


# url = f'{HOST}/sq4'
# ret = requests.request(method='GET', url=url)
# print(ret.json())

# url = f'{HOST}/333/gxt'
# ret = requests.request(method='GET', url=url)
# print(ret.text)

url = f'{HOST}/api/order/create/'
datas = {
    "user_id": "sq001",
    "goods_id": "1234",
    "num": 1,
    "amount": 100.8
}

ret = requests.request(method='POST', url=url, json=datas)
print(ret.json())
