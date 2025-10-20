# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：11_selenium爬取松勤课堂内容.py
@Date    ：2024/4/29 17:18 
'''
from time import sleep
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
# 浏览增加属性
options = webdriver.ChromeOptions()

# 无头浏览器配置headless
# options.add_argument('--headless')
options.add_argument("--disable-gpu")
# 无痕浏览器
options.add_argument("--incognito")
# 解决浏览器闪退问题
options.add_experimental_option('detach', True)
# 避免被侦测为自动化测试而拦截
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 模拟人为
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')

# 浏览器携带用户数据 user_data_dir，绕过大部分网站的登录
# user_data_dir = r"C:\Users\Echo\AppData\Local\Google\Chrome\User Data"
# options.add_argument(f'--user-data-dir={user_data_dir}')

# with webdriver.Chrome(options=options) as driver:
driver = webdriver.Chrome(options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    });
  """
})

driver.maximize_window()

driver.get('http://vip.ytesting.com/loginController.do?login2')
sel_cookies = driver.get_cookies()
print(sel_cookies)
# input(">>> 调试入口")
locator = 'id', 'userName'
WW(driver, 5, 0.5).until(EC.visibility_of_element_located(locator)).send_keys(
    'K202303211928')

locator = 'id', 'password'
WW(driver, 5, 0.5).until(EC.visibility_of_element_located(locator)).send_keys(
    '18500373250')

source_item = driver.find_element('id', 'nc_1_n1z')
start_item = source_item.rect['width']
end_item = driver.find_element('id', 'nc_1__scale_text').rect['width']
distance = end_item - start_item
ActionChains(driver).drag_and_drop_by_offset(source_item, distance, 0).perform()
sleep(1)
driver.find_element('id', 'but_login').click()

# print("end")
driver.save_screenshot('verify.png')
sleep(3)

flag = 11
if flag == 1:
    ...
    '''常规webdriver请求'''
    driver.execute_script("window.open('http://vip.ytesting.com/newsItemController.do?goContent&id=2c9f9b587eddaee2017f1a0c300a3e55')")

    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    '获取完整网页内容'
    locator = 'tag name', 'html'
    element = WW(driver, 30, 0.5).until(
        EC.visibility_of_element_located(locator))
    # element.encoding = 'utf8'

    print(element.text)


flag = 11
if flag == 1:
    ...
    '''将selenium的cookies同步到requests，发起请求'''
    # sel_cookies = driver.get_cookies()
    # print(sel_cookies)
    import requests
    jar = requests.cookies.RequestsCookieJar()
    for i in sel_cookies:
        # 将selenium侧获取的完整cookies的每一个cookie名称和值传入RequestsCookieJar对象
        # domain和path为可选参数，主要是当出现同名不同作用域的cookie时，为了防止后面同名的cookie将前者覆盖而添加的
        jar.set(i['name'], i['value'], domain=i['domain'], path=i['path'])
    print("jar >>>",jar)
    session = requests.session()  # requests以session会话形式访问网站
    session.cookies.update(jar)
    print('cookie1 >>>',session.cookies)

    url = 'http://vip.ytesting.com/newsItemController.do?goContent&id=2c9f9b587a4202a3017a4239eb150172'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    req = requests.Request(method='GET',url=url,headers=header)
    ret = session.send(session.prepare_request(req),verify=False, timeout=10)
    print('cookie2 >>>',session.cookies)

    print(ret.text)











