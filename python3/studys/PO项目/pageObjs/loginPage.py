# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : loginPage.py
@Time    : 2025/7/8 9:24
@Author  : Echo Wang
'''

from common.comm_driver import Env
from common.basePage import BasePage
from configs.allelements import Allelements

class LoginPage(BasePage):
    def open_test_url(self, url=Env.HOST):
        self.open_url(url)
        return self

    def login_test(self,username, password):
        ...



if __name__ == '__main__':
    lp = LoginPage()
    lp.open_test_url()
    flag = 11
    if flag == 1:
        ...
        locator = "id", "kw"
        lp.input_text(locator,"第一次输入")
        lp.input_text(locator,"第二次输入",True)
    flag = 1
    if flag == 1:
        ...
        lp = LoginPage()
        lp.open_test_url()
        locator = "css selector","#TANGRAM__PSP_3__footerULoginBtn"
        lp.click_element(locator)
        locator = "name","userName"
        lp.input_text(Allelements.USERNAME_LOCATOR, Allelements.username)
        lp.input_text(Allelements.PASSWORD_LOCATOR, Allelements.password)
        lp.click_element(Allelements.BUTTON_LOCATOR)
        print(lp.get_element_text(Allelements.BUTTON_LOCATOR))
        # 验证单例
        lp = LoginPage()
        lp.open_test_url()
        locator = "css selector", "#TANGRAM__PSP_3__footerULoginBtn"
        lp.click_element(locator)
        locator = "name", "userName"
        lp.input_text(Allelements.USERNAME_LOCATOR, Allelements.username)
        lp.input_text(Allelements.PASSWORD_LOCATOR, Allelements.password)
        lp.click_element(Allelements.BUTTON_LOCATOR)
        print(lp.get_element_text(Allelements.BUTTON_LOCATOR))

    if flag == 11:
        ...
        locator = "css selector",".tang-pass-footerBarULogin.pass-link"
        lp.click_element(locator)