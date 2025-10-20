# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : comm_driver.py
@Time    : 2025/7/7 17:16
@Author  : Echo Wang
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from configs.env import Env


# debug调试，锁定元素在控制台执行：setTimeout(()=>{debugger;},4000);

# 创建浏览器的单例模式调用
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)  # 创建实例
        # 如有实例，则直接返回实例
        return cls._instance


class Comm_Driver(Singleton):
    '''
    通用浏览器类
    '''
    driver = None
    def get_driver(self):
        # 避免被侦测为自动化测试而拦截
        if self.driver is None:
            if Env.headless_flag:
                if Env.browser_type == "chrome":
                    _option = webdriver.ChromeOptions()
                    _option.add_experimental_option('useAutomationExtension', False)
                    _option.add_experimental_option('excludeSwitches', ['enable-automation'])
                    _option.add_argument(
                        "--disable-blink-features=AutomationControlled")  # 禁用自动化特征检测

                    self.driver = webdriver.Chrome(options=_option)
                elif Env.browser_type == "firefox":
                    _option = webdriver.FirefoxOptions()
                    _option.set_preference("general.useragent.override",
                                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
                    self.driver = webdriver.Firefox(options=_option)
            else:
                if Env.browser_type == "chrome":
                    _option = webdriver.ChromeOptions()
                    _option.add_argument("--headless")
                    _option.add_experimental_option('useAutomationExtension', False)
                    _option.add_experimental_option('excludeSwitches', ['enable-automation'])
                    _option.add_argument(
                        "--disable-blink-features=AutomationControlled")  # 禁用自动化特征检测
                    self.driver = webdriver.Chrome(options=_option)
                elif Env.browser_type == "firefox":
                    _option = webdriver.FirefoxOptions()
                    _option.add_argument("--headless")
                    _option.set_preference("general.useragent.override",
                                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
                    self.driver = webdriver.Firefox(options=_option)

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            });
          """
        })
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(Env.page_load_timeout)
        return self.driver
