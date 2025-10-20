#-*- coding: utf-8 -*-
#@File    : test_shop.py
#@Time    : 2022/11/4 21:29
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2022/11/4
import pytest
import allure
import os
from utils.handle_excel_V3 import get_excel_data
from utils.handle_path import data_path, report_path
from common.apiAssert import ApiAssert
"""
fixture函数的调用：
    - 1.没有返回值的fixture函数，直接方法或者类前面使用  @pytest.mark.usefixtures('fixture函数名')
    - 2.有返回值的fixture函数：直接使用fixture函数名就行
        - 执行fixture函数里的代码
        - 拿到它的返回值
"""
@allure.epic('订餐系统')
@allure.feature('店铺模块')
@pytest.mark.shop
class TestShop:
    """ 店铺的测试类 """
    # def setup_class(self):
    #     print('setup_class...')
    @pytest.mark.parametrize('title,req_body,exp_data', get_excel_data('我的商铺','shopping'))
    @allure.story('店铺查询')
    @allure.title('{title}')
    def test_shop_query(self, shop_init,title,req_body,exp_data):
        print("test_shop_query")
        resp = shop_init.query(req_body)

        assert resp['code'] == exp_data['code']
    #@pytest.mark.skip('----暂时不运行----')
    @allure.story('店铺更新')
    def test_shop_update(self):
        print("test_shop_update")

if __name__ == '__main__':
    pytest.main([__file__, '-s','--alluredir', f'{report_path}', '--clean-alluredir'])
    os.system(f'allure serve {report_path}')
