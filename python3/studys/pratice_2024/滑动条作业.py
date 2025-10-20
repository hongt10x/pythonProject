# File_name: 滑动条作业
# Date: 2024-03-13
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
})
driver.maximize_window()
driver.get('http://vip.ytesting.com/loginController.do?login2')
driver.find_element(By.ID, 'userName').send_keys('S202309221001')
driver.find_element(By.ID, 'password').send_keys(1234321)
# 滑块
ele_k = driver.find_element(By.ID, 'nc_1_n1z')
# # 滑动条
ele_t = driver.find_element(By.ID, 'nc_1__scale_text')
# 距离
distance = ele_t.rect['width']-ele_k.rect['width']
# 执行鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
ac = ActionChains(driver)
ac.drag_and_drop_by_offset(ele_k, xoffset=distance, yoffset=0).perform()
sleep(1)
# 提交按钮
driver.find_element(By.ID, 'but_login').click()
driver.quit()