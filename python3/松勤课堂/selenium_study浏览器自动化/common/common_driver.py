# coding: utf8
# common_driver.py
# 2023/7/3
from selenium import webdriver
from selenium_study.config.env import Env


class Comm_Driver:
    def get_driver(self, browser_type='chrome', head_flag=Env.HEAD_FLAG):
        if head_flag:
            if browser_type == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser_type == 'firefox':
                self.driver = webdriver.Firefox()
        else:
            if browser_type == 'chrome':
                _option = webdriver.ChromeOptions()
                _option.add_argument('--headless')
                self.driver = webdriver.Chrome(options=_option)
            elif browser_type == 'firefox':
                _option = webdriver.FirefoxOptions()
                _option.add_argument('--headless')
                self.driver = webdriver.Firefox(options=_option)

        self.driver.maximize_window()
        # 页面加载最大超时时间set_page_load_timeout
        self.driver.set_page_load_timeout(Env.SET_PAGE_LOAD_TIMEOUT)
        return self.driver
