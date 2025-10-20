# coding: utf8
# loginPage.py
# 2023/7/3
from selenium_study.common.basePage import BasePage
from selenium_study.config.allElements import AllElements
from selenium_study.config.env import Env


class LoginPage(BasePage):
    def open_polly_loginpage(self, url=Env.HOSE):
        self.open_url(url)

    def login_polly(self):
        self.input_text(AllElements.USERNAME_LOCATOR, Env.USER_CONTENT)
        self.input_text(AllElements.PASSWORD_LOCATOR, Env.PWD_CONTENT)
        self.click_element(AllElements.LOGIN_BUTTON_LOCATOR)
