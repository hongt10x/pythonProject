from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
#

test_flag = 2
if test_flag == 1:
    driver.get('http://sahitest.com/demo/')
    driver.find_element('xpath', "//a[@href='clicks.htm']").click()
    ele_double_click = driver.find_element('xpath', "//*[@value='dbl click me']")
    ele_left_click = driver.find_element('xpath', "//*[@value='click me']")
    ele_right_click = driver.find_element('xpath', "//*[@value='right click me']")
    sleep(1)
    ActionChains(driver).double_click(ele_double_click).perform()
    sleep(1)
    ActionChains(driver).click(ele_left_click).perform()
    sleep(1)
    ActionChains(driver).context_click(ele_right_click).perform()

test_flag = 12
if test_flag == 1:
    driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
    start_item = driver.find_element('id', 'dragger')
    end_items = driver.find_elements('css selector', '.item')
    # print(ends,type(ends))
    # for end_item in end_items:
    #     ActionChains(driver).drag_and_drop(start_item, end_item).perform()
    #     sleep(1)
    myaction = ActionChains(driver)
    for _ in end_items:
        myaction.click_and_hold(start_item)
        myaction.release(_)
        print("hello, start move")
        myaction.perform()
        sleep(1)

test_flag = 1
if test_flag == 1:
    driver.get('http://vip.ytesting.com/loginController.do?login')
    sleep(1)
    driver.find_element('id', 'userName').send_keys('K202303211928')
    # sleep(1)
    driver.find_element('id', 'password').send_keys('18500373250')
    # sleep(1)
    source_item = driver.find_element('id', 'nc_1_n1z')
    start_item = source_item.rect['width']
    print(start_item)
    end_item = driver.find_element('id', 'nc_1__scale_text').rect['width']
    print(end_item)
    distance = end_item - start_item
    ActionChains(driver).drag_and_drop_by_offset(source_item, distance, 0).perform()
    # sleep(1)
    driver.find_element('id', 'but_login').click()

test_flag = 11
if test_flag == 1:
    driver.get('http://121.5.150.55:8090/forum.php')
    sleep(1)
    ele_item = driver.find_element('css selector', '.pn.vm')
    ele = ele_item.rect
    print(ele)
    x = ele['x'] + ele['width'] / 2
    y = ele['y'] + ele['height'] / 2
    myaction = ActionChains(driver)
    myaction.move_by_offset(x, y).click().perform()


test_flag = 11
if test_flag == 1:
    driver.get('http://www.baidu.com')
    sleep(1)
    driver.find_element('css selector','#kw').send_keys('python \n')
    sleep(1)
    driver.back()
    sleep(1)
    driver.forward()
    sleep(1)
    driver.refresh()






