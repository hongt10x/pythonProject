# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：loginRSA.py
@Date    ：2024/2/23 11:00 
'''

import requests
from utils.encrypt_data import get_md5_data
from utils.encrypt_data import RsaEndecrypt

HOST = 'http://42.192.62.8:8082'


def login(in_data: dict):
    url = f'{HOST}/account/loginRsa'

    # 1.对密码进行md5加密
    pwd_md5_text = get_md5_data(in_data['password'])
    # 2.对加密后的密文进行rsa加密
    pwd_rsa_text = RsaEndecrypt('../utils/').encrypt(pwd_md5_text)
    print(pwd_rsa_text)
    # 3.把加密后的结果赋值给原密码
    in_data['password'] = pwd_rsa_text

    # 4.增加sign签名
    in_data.update({'sign': get_md5_data(in_data['username'] + pwd_rsa_text)})

    payload = in_data
    resp = requests.post(url, data=payload)

    print(resp.text)
    print(resp.request.body)


if __name__ == '__main__':
    data = {
        "username": "yp0731",
        "password": "17805"
    }
    login(data)
