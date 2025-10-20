# coding: utf8
# basePage.py
# 2023/7/3

from selenium_study.common.common_driver import Comm_Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_study.config import allElements
from selenium_study.config.env import Env


class BasePage:
    def __init__(self):
        self.driver = Comm_Driver().get_driver()

    def open_url(self, url):
        self.driver.get(url)

    def get_element_old(self, locator):
        return self.driver.find_element(*locator)

    def get_element(self, locator, timeout=Env.TIMEOUT, poll_freq=Env.POLL_FREQUENCY):
        # 元素查找显式等待
        return WebDriverWait(self.driver, timeout, poll_freq).until(EC.visibility_of_element_located(locator))

    def input_text_old(self, locator, text):
        import warnings
        warnings.warn('This method will be removed ! Please use new method replace it !')
        self.get_element(locator).send_keys(text)

    def input_text(self, locator, text, append=True):
        if not append:
            self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_element_text(self, locator):
        return self.get_element(locator).text


if __name__ == '__main__':
    basepage = BasePage()
    basepage.open_url(url=Env.HOSE)
    basepage.input_text_old(allElements.AllElements.USERNAME_LOCATOR, '朝天宫234')
