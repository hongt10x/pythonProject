# -*- coding: utf-8 -*-
# @File    : handle_mock.py
# @Time    : 2023-05-22 20:29
# @Author  : xintian
# @Email   : 1730588479@qq.com
# @Software: PyCharm
# Date:2023-05-22
import requests
import time
import threading
HOST = 'http://127.0.0.1:9999'

# 1. 提交退订申请订单


def commit_order(in_data):
    url = f'{HOST}/api/order/create/'
    resp = requests.post(url, json=in_data)
    return resp.json()

# 2. 查询结果
"""
功能：查询接口--异步查询!
注意事项：
    1- 使用对应的id去查询；
    2- 查询不是只查询一次，一直 频率  5s
    3- 如果查询一定时间，还是没有结果，需要一个超时机制！
"""
def get_order_result(id, interval=5, time_out=30):
    """
    :param id:  申请的id
    :param interval: 查询频率 单位 s
    :param time_out: 超时时间 单位 s
    :return: 结果！
    """
    url = f'{HOST}/api/order/get_result01/'
    payload = {'order_id': id}
    start_time = time.time()  # 开始时间
    end_time = start_time + time_out  # 结束时间
    cnt = 1  # 查询次数
    while time.time() < end_time:
        resp = requests.get(url, params=payload)  # 查询操作
        if resp.text:  # 查询到内容
            print(f'第{cnt}次查询结束，结果--->', resp.text)
            return
        else:
            print(f'第{cnt}次查询没有结果，请稍微查询！')

        time.sleep(interval)  # 频率
        cnt += 1

    print('查询超时，请联系平台管理员！')






if __name__ == '__main__':
    start_time = time.time() # 主线程开始计时
    # 1. 提交申请的信息
    order_info = {
        "user_id": "sq123456",
        "goods_id": "20200815",
        "num": 1,
        "amount": 200.6}
    id = commit_order(order_info)['order_id']
    print(id)
    # 2. 调用查询接口
    #---------------------创建子线程---异步查询接口----------------
    # target=需要把哪一个函数做成子线程，直接写这个函数的函数名！
    # t1 = threading.Thread(target=get_order_result, args=(id,))
    # # 主线程如果结束，子线程全部退出
    # t1.setDaemon(True)
    # t1.start()  # 开始运行！

    # get_order_result(id)

    # 主线程处理其他接口自动化测试
    for one in range(20):
        print(f'---{one}>>> 我正在执行其他接口的自动化测试！')
        time.sleep(1)  # 模拟接口操作时间
    end_time = time.time()
    print(f'整个自动化测试耗时>>>{end_time-start_time}s')


"""
向我们需要思考的事情：
代码编写的阶段：
    1- 基本逻辑功能实现！
    2- 优化阶段: 代码结构+执行效率(性能/资源)
完成任务跟领导沟通：
    领导：功能是否可以实现！，运行给他看看，发现你的执行效率比较低！
分析领导的需求
    1- 领导说的是一个 现象
    2- 查询接口的间隔时间中是没有充分利用！
解决方案：
    1- 细致分析: 没有利用好cpu资源
        - cpu 高运算
        - cpu io阻塞
            - request
            - sleep
    2- 如何提高效率： 充分使用sleep 间隔的5s时间
        - 多线程 充分使用一个cpu核  core ： 一个进程里可以创建多个线程！
        - 多进程 使用多个核
        - 协程 比线程好用点
        - 多进程+协程
    实现：
        - 主线程： main主要代码（其他接口的业务）
        - 子线程：查询接口
    扩展技术：
        pytest有自己多线程插件 
        pytest有自己多进程插件 pytest-xdist
"""