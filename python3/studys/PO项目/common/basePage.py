# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : basePage.py
@Time    : 2025/7/7 17:29
@Author  : Echo Wang
'''
from common.comm_driver import Comm_Driver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
import warnings


class BasePage:
    '''
    点击元素
    输入文本...
    '''

    def __init__(self):
        self.driver = Comm_Driver().get_driver()

    def open_url(self, url):
        '''
        本地url
        互联网url
        :param url:
        :return:
        '''
        self.driver.get(url)

    def get_element_old(self, locator):
        '''
        定位元素
        :param locator:
        :return:
        '''

        warnings.warn("This method was deprecated ! Please use 'get_element' method "
                      "instead !",
                      DeprecationWarning)
        return self.driver.find_element(*locator)

    def get_element(self, locator):
        return WW(self.driver, 10, 0.5).until(EC.visibility_of_element_located(locator))

    def input_text_old(self, locator, text):
        warnings.warn("This method was deprecated ! Please use 'input_text' method "
                      "instead !",
                      DeprecationWarning)
        # 产生删除线
        self.get_element(locator).send_keys(text)

    def input_text(self, locator, text, append=False):  # 是否追加内容判断
        if append:
            self.get_element(locator).send_keys(text)
        else:
            self.get_element(locator).clear()
            self.get_element(locator).send_keys(text)

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_element_text(self, locator):
        return self.get_element(locator).text

    def to_be_that(self, url):
        '''是否是指定的url'''
        return WW(self.driver, 5, 0.5).until(EC.url_to_be(url))


if __name__ == '__main__':
    bp = BasePage()
    bp.open_url("https://www.baidu.com")
    # from time import sleep
    # sleep(1)

    # print(bp.to_be_that('https://www.baidu.com'))
    locator = "id", "kw"
    # bp.input_text(locator,"第一次输入")
    # bp.input_text(locator,"第二次输入",True)
    bp.input_text_old(locator, "做一次测试")  # deprecated
    bp.input_text_old(locator, "做二次测试\n")
    # print(bp.to_be_that(r'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%81%9A%E4%B8%80%E6%AC%A1%E6%B5%8B%E8%AF%95%E5%81%9A%E4%BA%8C%E6%AC%A1%E6%B5%8B%E8%AF%95&fenlei=256&rsv_pq=0x99ab157e00011351&rsv_t=647eV3ZrdsnfldlqxtKLx%2FqvefcTObOsQhRMYMa1Z7J4Ab%2F9lcs4JGNh2c9A&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=10&rsv_sug2=0&rsv_btype=i&inputT=170&rsv_sug4=169'))