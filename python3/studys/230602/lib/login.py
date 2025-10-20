# -*- coding: utf-8 -*-
import requests

from utils.handle_rsa import get_md5_data
from utils.handle_rsa import RsaObj


def login(data: dict):
    url = 'http://42.192.62.8:8082/account/loginRsa'
    data_md5 = get_md5_data(data['password'])
    print(data_md5)
    pwd_rsa = RsaObj().get_rsa(data_md5)
    data['password'] =pwd_rsa
    #
    sign_data = get_md5_data(data['username'] + pwd_rsa)
    data.update({'sign': sign_data})

    res = requests.post(url, data=data)
    print(res.text)


if __name__ == '__main__':
    login_data = {'username': 'th0198', 'password': 'xintian'}
    login(login_data)
