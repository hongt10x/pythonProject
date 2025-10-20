# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250725-性能探究.py
@Time    : 2025/7/25 15:02
@Author  : Echo Wang
'''

flag = 11
if flag == 1:
    ...
    import timeit


    # 普通循环
    def square_with_loop(n):
        result = []
        for i in range(n):
            result.append(i ** 2)
        return result


    # 列表推导式
    def square_with_comprehension(n):
        return [i ** 2 for i in range(n)]


    # 性能对比
    n = 1000000
    print("普通循环:", timeit.timeit(lambda: square_with_loop(n), number=10))
    print("列表推导式:", timeit.timeit(lambda: square_with_comprehension(n), number=10))

flag = 11
if flag == 1:
    ...
    # 多线程处理
    import requests
    from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

    URLS = [
        "https://example.com",
        "https://sahitest.com/demo/",
        "https://w3c.github.io/webdriver/#endpoints",
        # ... 共100个url
    ]


    def download_single(url):
        try:
            response = requests.get(url, timeout=5)
            return url, response.status_code
        except:
            return url, None


    def download_with_threads():
        with ThreadPoolExecutor(max_workers=10) as executor:
            result = list(executor.map(download_single, URLS))
        return result


    def download_with_processes():
        with ProcessPoolExecutor(max_workers=2) as executor:
            result = list(executor.map(download_single, URLS))
        return result


    # 性能比对
    import time

    start = time.time()
    download_with_threads()
    print("多线程耗时：", time.time() - start)

    start = time.time()
    download_with_processes()  # 多进程会报错
    print("多进程耗时：", time.time() - start)

flag = 11
if flag == 1:
    ...
    import numpy as np
    import random
    import timeit


    # 纯 Python 实现
    def sum_with_python(n):
        data = [random.random() for _ in range(n)]
        return sum(data)


    # NumPy 实现
    def sum_with_numpy(n):
        data = np.random.randint(n, size=n)  # 0.745s，randint耗时比rand多1倍
        # data = np.random.rand(n)  # 0.365s
        return np.sum(data)


    # 性能对比
    n = 10000000
    print("纯 Python 耗时:", timeit.timeit(lambda: sum_with_python(n), number=5))
    print("NumPy 耗时:", timeit.timeit(lambda: sum_with_numpy(n), number=5))

flag = 11
if flag == 1:
    ...
    import numpy as np1

    n1 = 10
    # ret1 = np1.random.rand(n1)
    # ret1 = np1.random.randint(n1, size=n1)
    ret1 = np1.random.randint(n1, size=(n1, n1))
    print(ret1)

flag = 11
if flag == 1:
    ...
    from functools import lru_cache
    from timeit import timeit


    # 无缓存递归
    def fib_no_cache(n):
        if n <= 1:
            return n
        return fib_no_cache(n - 1) + fib_no_cache(n - 2)


    n2 = 50
    # print(fib_no_cache(n2))
    print(timeit(lambda: fib_no_cache(n2), number=2))


    # import sys
    # print(sys.getrecursionlimit())  # 最大递归次数为1000

    @lru_cache(maxsize=None)
    def fib_with_cache(n):
        if n <= 1:
            return n
        return fib_with_cache(n - 1) + fib_with_cache(n - 2)


    print(timeit(lambda: fib_with_cache(n2), number=100))

flag = 1111
if flag == 1:
    ...
    from functools import lru_cache
    import timeit

    class HumanTimeit:
        def __init__(self, stmt="pass", setup="pass", number=1, repeat=3):
            self.stmt = stmt
            self.setup = setup
            self.number = number
            self.repeat = repeat

        def run(self):
            timer = timeit.Timer(self.stmt, self.setup)
            raw_times = timer.repeat(self.repeat, self.number)
            best_time = min(raw_times) / self.number

            # 自动选择单位
            if best_time >= 1:
                unit, scale = "s", 1
            elif best_time >= 1e-3:
                unit, scale = "ms", 1e3
            elif best_time >= 1e-6:
                unit, scale = "μs", 1e6
            else:
                unit, scale = "ns", 1e9

            human_time = best_time * scale
            return f"{human_time:.3f} {unit}"

        # 无缓存的递归（极慢）


    def fib_no_cache_1(self, n):
        if n <= 1:
            return n
        return fib_no_cache_1(n - 1) + fib_no_cache_1(n - 2)

        # 带缓存的递归（极快）
        # @lru_cache(maxsize=None)


    @lru_cache()
    def fib_with_cache_1(self, n):
        if n <= 1:
            return n
        return fib_with_cache_1(n - 1) + fib_with_cache_1(n - 2)


    # 性能对比
    # 示例用法
    timer = HumanTimeit()
    print("无缓存 fib(35) 耗时:", timeit.timeit(lambda: timer.run(), number=1))
    timer = HumanTimeit("fib_with_cache(35)")
    print("带缓存 fib(35) 耗时:", timeit.timeit(lambda: timer.run(), number=1))


flag = 1
if flag == 1:
    ...
    from functools import lru_cache










