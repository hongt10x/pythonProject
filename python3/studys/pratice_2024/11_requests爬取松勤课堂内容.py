# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：11_requests爬取松勤课堂内容.py
@Date    ：2024/4/29 17:18 
'''
from time import sleep
import requests
import json
session = requests.session()
url = 'http://vip.ytesting.com/loginController.do?login'

userName = 'K202303211928'
password = '18500373250'

user_info = {
    'userName': 'K202303211928',
    'password': '18500373250',
    'Sig': '05XqrtZ0EaFgmmqIQes-s-CAIXd4Eyp-KLuf4bmnvABlr9JVxnqiFNBzTTOBAG045WgDPykDZO595RJ998sdbbG7S5920o3WXOWWgngrYzsoRg7wEoevct_fcCivXMzeYLE4Sg87t9Saz_HKeVOraauxwTkiKH7HJnsok9qTAk6oKNikV4d520gTIoE7esBJTVngRmIzsJNe9wt_JsRuDaffdkrzImU46BQIgM3ZoceTtb7-ktPYkuTgJJeu1YK86ClV4ycwERlm-zYXXLOTxeOZhGUKfXA66uB8zTeCNghEXzbG66sT6sNRaK65SKZ5vPHuWPk8wQLtowh3CU9F4ZqYDSwfW9bfRoJmz4w7mCer02G6SqpCxhX0o_mjvuSwbRTwhyc0EffHGXWrUHPhSWAA',
    'bsq030': ''
}

# ret = session.request('GET',url, data=json.dumps(user_info))
ret = session.get(url, params=user_info)
print(ret.cookies)

url = 'http://vip.ytesting.com/newsItemController.do?goContent&id=2c9f9b587a4202a3017a4239eb150172'
resp = session.get(url)
print(resp.text)

flag = 11
if flag == 1:
    ...

    url = 'http://vip.ytesting.com/newsItemController.do?goContent&id=2c9f9b587a4202a3017a4239eb150172'

    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait as WW
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.Chrome()
    driver.add_cookie(ret.cookies)
    print(driver.get_cookies())
flag = 11
if flag == 1:
    ...

    driver.get(url)

    '获取完整网页内容'
    locator = 'tag name', 'html'
    element = WW(driver, 30, 0.5).until(EC.visibility_of_element_located(locator))
    # element.encoding = 'utf8'

    print(element.text)


# <RequestsCookieJar[<Cookie JSESSIONID1=91D614758D6A03144F4C7A5E2F76CC69 for vip.ytesting.com/>]>