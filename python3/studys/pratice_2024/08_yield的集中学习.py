# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：08_yield的集中学习.py
@Date    ：2024/4/22 13:46 
'''

flag = 11
if flag == 1:
    ...

    def gen():
        yield from 'A'
        # yield from range(1, 4)

    def gen1():
        yield 'A'
        # yield from range(1, 4)

    print(next(gen()))
    print(next(gen1()))

flag = 11
if flag == 1:
    ...


    def fib(n):
        index = 0
        a = 0
        b = 1

        while index < n:
            yield b
            a, b = b, a + b
            index += 1


    f = fib(5)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))

flag = 11
if flag == 1:
    ...
    import time


    def fib(n):
        index = 0
        a = 0
        b = 1

        while index < n:
            sleep = yield b
            print('等待%s秒' % sleep)
            time.sleep(sleep)
            a, b = b, a + b
            index += 1


    fib = fib(20)
    print(fib.send(None))  # 效果等同于print(next(fib))
    print(fib.send(2))
    print(fib.send(3))
    print(fib.send(4))
    # print(fib.send(2))

flag = 10
if flag == 1:
    ...


    def fun_inner():
        i = 0
        while True:
            i = yield i
            # print(f'fun_inner: {i}')


    def fun_outer():
        a = 0
        b = 1
        inner = fun_inner()
        inner.send(None)
        while True:
            a = inner.send(b)
            b = yield a
            # print(f'fun_outer: {a} {b}')


    if __name__ == '__main__':
        outer = fun_outer()
        outer.send(None)
        for i in range(5):
            print(outer.send(i))

flag = 11
if flag == 1:
    ...


    def fun_inner():
        i = 0
        while True:
            i = yield i


    def fun_outer():
        yield from fun_inner()


    if __name__ == '__main__':
        outer = fun_outer()
        outer.send(None)
        for i in range(5):
            print(outer.send(i))


flag = 11
if flag == 1:
    ...


    # 子生成器
    def average_gen():
        total = 0
        count = 0
        average = 0
        while True:
            new_num = yield average
            if new_num is None:
                break
            count += 1
            total += new_num
            average = total / count

        # 每一次return，都意味着当前协程结束。
        return total, count, average


    # 委托生成器
    # 委托生成器，只起一个桥梁作用，它建立的是一个双向通道，它并没有权利也没有办法，对子生成器yield回来的内容做拦截
    def proxy_gen():
        while True:
            # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
            total, count, average = yield from average_gen()
            print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))


    # 调用方
    def main():
        calc_average = proxy_gen()
        next(calc_average)  # 预激协程
        print(calc_average.send(10))  # 打印：10.0
        print(calc_average.send(20))  # 打印：15.0
        print(calc_average.send(30))  # 打印：20.0
        calc_average.send(None)  # 结束协程
        # 如果此处再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程
    '''输出
    10.0
    15.0
    20.0
    计算完毕！！
    总共传入 3 个数值， 总和：60，平均数：20.0
    '''

    if __name__ == '__main__':
        main()

flag = 11
if flag == 1:
    ...


    # 子生成器
    def average_gen():
        total = 0
        count = 0
        average = 0
        while True:
            new_num = yield average
            if new_num is None:
                break
            count += 1
            total += new_num
            average = total / count


    # 委托生成器
    def proxy_gen():
        while True:
            print('*'*40)
            yield from average_gen()
            print('+' * 40)


    # 调用方
    def main():
        calc_average = proxy_gen()
        next(calc_average)  # 预激下生成器
        print(calc_average.send(10))  # 打印：10.0
        print(calc_average.send(20))  # 打印：15.0
        print(calc_average.send(30))  # 打印：20.0
        calc_average.send(None)


    if __name__ == '__main__':
        main()


flag = 1
if flag == 1:
    ...


    # 子生成器
    def average_gen():
        total = 0
        count = 0
        average = 0
        while True:
            new_num = yield average
            if new_num is None:
                break
            count += 1
            total += new_num
            average = total / count
        return 'average'


    # 委托生成器
    def proxy_gen():
        while True:
            print('*'*40)
            xx = yield from average_gen()
            print('+' * 40,xx)


    # 调用方
    def main():
        calc_average = proxy_gen()
        next(calc_average)  # 预激下生成器
        print(calc_average.send(10))  # 打印：10.0
        print(calc_average.send(20))  # 打印：15.0
        print(calc_average.send(30))  # 打印：20.0
        # calc_average.send(None)
        next(calc_average)
        next(calc_average)
        next(calc_average)
        print(calc_average.send(40))  # 打印：20.0

    if __name__ == '__main__':
        main()

