# -*- coding: utf-8 -*-
# time: 2023/7/6 10:56
# file: handle_rsa.py
# author: wht

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKC
import base64
import os


class RsaObj:
    def get_rsa(self, data):
        # 获取公钥
        with open('./public.pem', 'rb') as f:
            cryp_text = f.read()
        # 编码原始数据
        origin_data = data.encode('utf-8')
        # 导入公钥，生成公钥对象
        cryp_text_obj = RSA.importKey(cryp_text)
        # 生成加密对象
        cryp_new = PKC.new(cryp_text_obj)
        # 开始加密
        cryp_encypt_text = cryp_new.encrypt(origin_data)
        return base64.b64encode(cryp_encypt_text).decode('utf-8')


if __name__ == '__main__':
    data = '123456'
    obj = RsaObj()
    print(obj.get_rsa(data))
