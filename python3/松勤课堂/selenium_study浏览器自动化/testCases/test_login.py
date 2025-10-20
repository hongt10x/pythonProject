# coding: utf8
# test_login.py
# 2023/7/3

import pytest

from selenium_study.config.allElements import AllElements
from selenium_study.pageObjs.loginPage import LoginPage


def test_login1():
    test_loginpage = LoginPage()
    test_loginpage.open_polly_loginpage()
    test_loginpage.login_polly()
    assert test_loginpage.get_element_text(AllElements.MAINPAGE_LOCATOR) == '首页'


if __name__ == '__main__':
    pytest.main(['-sv', __file__])
