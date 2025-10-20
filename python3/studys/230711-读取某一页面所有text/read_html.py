# -*- coding: utf-8 -*-
# time: 2023/7/11 15:31
# file: read_html.py
# author: wht

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW
import io
import sys

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

start_time = time.monotonic()
options = webdriver.ChromeOptions()
# 无头浏览
options.add_argument('--headless')

# 浏览器携带用户数据 user_data_dir，绕过大部分网站的登录
# user_data_dir = r"C:\Users\Echo\AppData\Local\Google\Chrome\User Data"
# options.add_argument(f'--user-data-dir={user_data_dir}')

# 避免被侦测为自动化测试而拦截
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# WebDriver的页面加载策略:
# 默认情况下，SeleniumWebDriver在加载页面时，根据正常的加载策略，就是把get地址的页面及所有静态资源都下载完（如css、图片、js等）。
# normal （默认）：所有内容加载完成，包括文件、css、js等。
# eager：等待初始HTML文档完全加载和解析，并放弃css、图像和子框架的加载。
# none：仅等待初始页面下载即可操作。
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    });
  """
})

mid2_time = time.monotonic()
print('>>>>>>>> 无头浏览器启动时长为：', mid2_time - start_time)

test_flag = 1
if test_flag == 1:
    start_time1 = time.monotonic()

    # 把要查询的url连接替换掉此处即可

    url = r'''
    
        
        
        https://blog.csdn.net/zxy_666/article/details/80173288
        
        
          
        '''

    # 把要查询的url连接替换掉此处即可

    driver.get(url)
    mid1_time = time.monotonic()
    print('>>>>>>>> 打开网页时长为：', mid1_time - start_time1)

    '2024/4/16  定位整个网页内容；如果是知乎网页，需要关闭固定的登录窗口，否则会影响爬取数据的完整性'
    try:
        if '.zhihu.' in url:
            locator = 'css selector', '.Zi.Zi--Close.Modal-closeIcon'
            WW(driver, 5, 0.5).until(
                EC.visibility_of_element_located(locator)).click()
            time.sleep(0.5)  # 需要强制等待一下，否则数据获取不全
    except:
        pass

    '获取完整网页内容'
    locator = 'tag name', 'html'
    element = WW(driver, 30, 0.5).until(
        EC.visibility_of_element_located(locator))
    # element.encoding = 'utf8'

    end_time = time.monotonic()
    print(">>>>>>>> 完成定位查询总时长为：", end_time - start_time)

    time.sleep(0.5)
    print(element.text)

    # driver.quit()
