# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：reqeust的参数--get请求用params--post请求用data.py
@Date    ：2024/1/29 15:53 
'''
import pprint

import requests

dic = {"name":"kee","age":26,'addr':"forest"}
url ='https://httpbin.org/post'
# req =  requests.request('POST',url,data=dic)
# print(url)
# print(req.text)
#
# req =  requests.request('POST',url,json=dic)
# print(url)
# pprint.pp(req.json())

flag = 11
if flag == 1:
    ...

    print("*"*40)
    req= requests.request('POST',url,params=dic)
    print(url)
    print(req.text)
    ret = req.json()
    print(type(ret),ret['url'])
    #
    print("="*40)
    url ='https://httpbin.org/get'
    req= requests.request('GET',url,params=dic)
    print(url)
    print(req.text)
    ret = req.json()
    print(type(ret),ret['url'])

    req =  requests.request('GET',url,data=dic)
    print(url)
    print(req.text)

    print("--"*40)
    url ='https://httpbin.org/post'
    req =  requests.request('POST',url,data=dic)
    print(url)
    print(req.text)


    print("+"*40)
    url ='https://httpbin.org/post'
    req =  requests.request('POST',url,json=dic)
    print(url)
    print(req.text)
    print(req.json())


print("&"*40)
url ='https://httpbin.org/get'
req= requests.request('GET',url,json=dic)
print(url)
print(req.text)


