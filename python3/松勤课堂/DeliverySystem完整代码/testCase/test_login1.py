# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：test_login1.py
@Date    ：2024/2/27 9:58 
'''
import os

import pytest
import allure
from libs.login import Login
from utils.handle_excel_V3 import get_excel_data

@allure.epic('订餐系统')
@allure.feature('登录模块')


class TestLogin:
    @pytest.mark.parametrize('title,req_body,exp_data',get_excel_data('登录模块', 'Login'))
    @allure.story('登录接口')
    @allure.title('{title}')
    def test_login(self,title,req_body,exp_data):
        # print("req_body:",req_body)
        # print("exp_data:",exp_data)
        res = Login().login(req_body)
        assert res['msg'] ==  exp_data['msg']

if __name__ == '__main__':
    pytest.main([__file__, '-s','--alluredir','../outFiles/report/tmp','--clean-alluredir'])
    os.system('allure serve ../outFiles/report/tmp')



