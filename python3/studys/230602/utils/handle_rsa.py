# -*- coding: utf-8 -*-
# time: 2023/7/6 10:56
# file: handle_rsa.py
# author: wht


import hashlib
def get_md5_data(data: str):
    hash_obj = hashlib.md5()
    new_data = data.encode('utf-8')
    hash_obj.update(new_data)
    return hash_obj.hexdigest()




from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKC
import base64
import os
from common.base_path import utils_path

class RsaObj:
    def get_rsa(self, data):
        # 获取公钥
        with open(os.path.join(utils_path,'public.pem'), 'rb') as f:
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
    print(get_md5_data(data))
    obj = RsaObj()
    print(obj.get_rsa(data))
