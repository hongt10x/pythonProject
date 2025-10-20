# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250822-yield深度体验.py
@Time    : 2025/8/22 10:57
@Author  : Echo Wang
'''

flag = 11
if flag == 1:
    ...


    # 基本 yield	yield 1	暂停并返回一个值
    def sub_gen():
        a = yield 1
        print(f"a: {a}")
        b = yield 2
        print(f"b: {b}")
        yield 3


    #
    x = sub_gen()
    print("#" * 20)
    print(next(x))
    print("#"*20)
    print(x.send("xxxxx"))
    print("#" * 20)
    print(x.send("yyyy"))
    print("#" * 20)

    def main_gen():
        k = yield from sub_gen()
        print(f"k:{k}")
        yield from [5, 4]


    print(list(main_gen()))

flag = 11
if flag == 1:
    ...


    def interactive_generator():
        value = yield "Start"  # 第一次 yield 返回 "Start"，并等待 send() 传值
        print(f"Received: {value}")
        yield "Next"
        yield "End"


    print(interactive_generator().__next__())
    print(interactive_generator().__next__())
    # gen = interactive_generator()
    # print(next(gen))
    # print(gen.send(100))
    # print(next(gen))

flag = 11
if flag == 1:
    ...


    def even_numbers(n):
        for i in range(n):
            if i % 2 == 0:
                yield i  # 只返回偶数


    print(list(even_numbers(10)))  # 输出: [0, 2, 4, 6, 8]

    print(list(x for x in range(10) if x % 2 == 0))

flag = 11
if flag == 1:
    ...


    def infinite_generator():
        try:
            while True:
                yield "Running..."
        except GeneratorExit:
            print("Generator closed!")
        except Exception as e:
            print(f"Generator received exception: {e}")


    # 控制生成器	gen.close(), gen.throw()	手动关闭或抛出异常
    gen = infinite_generator()
    print(next(gen))  # 输出: "Running..."
    gen.close()  # 输出: "Generator closed!"

    gen = infinite_generator()
    print(next(gen))  # 输出: "Running..."
    gen.throw(ValueError("Oops!"))  # 输出: "Generator received exception: Oops!"

flag = 11
if flag == 1:
    ...


    # 生成器可以很好地实现状态机模式：
    def state_machine():
        state = 'start'
        while True:
            if state == 'start':
                action = yield 'waiting for input'
                if action == 'go':
                    state = 'running'
            elif state == 'running':
                action = yield 'processing'
                if action == 'stop':
                    state = 'stopped'
            elif state == 'stopped':
                yield 'done'
                break


    sm = state_machine()
    print(next(sm))  # 输出: waiting for input
    print(sm.send('go'))  # 输出: processing
    print(sm.send('stop'))  # 输出: done

flag = 11
if flag == 1:
    ...


    def double_input():
        while True:
            value = yield
            yield value * 2


    gen = double_input()
    next(gen)
    print(gen.send(5))  # 输出: 10
    next(gen)
    print(gen.send(7))  # 输出: 14

flag = 11
if flag == 1:
    ...


    def delicate_generator():
        try:
            yield 1
            yield 2

        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except Exception as e:
            print(f"Exception Error: {e}")
        finally:
            print("Generator cleaning up")


    gen = delicate_generator()
    print(next(gen))  # 输出: 1
    # gen.throw(ValueError)  # 输出: Caught ValueError
    gen.throw(ValueError("god please !"))  # 输出: Caught ValueError

    # 输出: Generator cleaning up

flag = 11
if flag == 1:
    ...


    # 生成器可以递归调用自身

    def flatten(nested):
        for sublist in nested:
            if isinstance(sublist, (list, tuple)):
                yield from flatten(sublist)
            else:
                yield sublist


    list(flatten([1, [2, [3, 4], 5], (13, 14), 6]))  # 输出: [1, 2, 3, 4, 5, 6]
    print(list(flatten([1, [2, [3, 4], 5], (13, 14), 6])))

flag = 11
if flag == 1:
    ...


    # 将多个数据处理阶段连接起来：
    def reader(filename):
        with open(filename, encoding="utf-8") as f:
            yield from (line.strip() for line in f)


    def filterer(lines):
        yield from (line for line in lines if "python" in line)


    def counter(lines):
        count = 0
        for line in lines:
            count += 1
            yield count, line


    # 构建处理管道
    pipeline = counter(filterer(reader("example.txt")))
    for line_num, content in pipeline:
        print(f"{line_num}: {content}")

flag = 11
if flag == 1:
    ...


    def sub_gen():
        try:
            yield 1
            yield 2
        except ValueError as e:
            print(f"Sub gen caught: {e}")
            yield "Error handled"


    def main_gen():
        yield from sub_gen()


    gen = main_gen()
    print(next(gen))  # 输出: 1
    print("*" * 20)
    print(next(gen))  # 输出: 2
    print("*" * 20)
    print(gen.throw(ValueError("Oops")))  # 输出: "Sub gen caught: Oops" → "Error handled"
    print("*" * 20)
    # gen.close()

flag = 1
if flag == 1:
    ...


    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right


    def inorder(node):
        if node:
            yield from inorder(node.left)
            yield node.value
            yield from inorder(node.right)


    # 构建二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3))
    print(list(inorder(tree)))  # 输出: [4, 2, 5, 1, 3]

flag = 11
if flag == 1:
    ...


    def inner():
        value = yield "inner yield"
        print(f"Inner received: {value}")
        yield "inner done"


    def outer():
        print("Entering outer")
        yield from inner()
        print("Exiting outer")


    gen = outer()
    print(next(gen))  # 启动生成器，输出 "inner yield"
    gen.send("Hello")  # 发送值到 inner()，输出 "Inner received: Hello"，然后抛出 StopIteration

flag = 11
if flag == 1:
    ...


    def bad_inner():
        yield 1  # 没有接收 send 的值
        yield 2


    def outer():
        yield from bad_inner()


    print("start...")
    gen = outer()
    print(next(gen))
    print(gen.send("foo"))
    print("end...")

flag = 11
if flag == 1:
    ...


    def inner():
        value = yield "Ready to receive"
        print(f"Inner got: {value}")
        yield "Inner finished"


    def outer():
        print("Starting outer")
        result = yield from inner()
        print(f"Outer got return: {result}")
        yield "Outer done"


    gen = outer()
    print(next(gen))  # 输出 "Ready to receive"
    print(gen.send("Hello"))  # 输出 "Inner got: Hello"，然后 "Inner finished"
    try:
        gen.send("World")  # 外部生成器的下一个 yield 是 "Outer done"，但此时已无 yield，抛出 StopIteration
    except StopIteration:
        print("Generator ended")

flag = 11
if flag == 1:
    ...


    def t1():
        for i in range(3):
            yield i
        print("=" * 20)
        value = yield "t1 end..."
        print(f"t1....{value}")


    def t2():
        print("t2 start...")
        value = yield from t1()
        yield f"t2 end...{value}"


    t = t2()
    # for _ in t:
    #     print(_)
    print(next(t))
    print(next(t))
    print(next(t))
    print(next(t))
    print(t.send("xxxx"))
    print(t.send("yyyy"))
    # print(next(t))

flag = 11
if flag == 1:
    ...


    def t1():
        for i in range(3):
            yield i
        print("=" * 20)
        value = yield "t1 end..."
        print(f"t1....{value}")
        return value


    def t2():
        print("t2 start...")
        value = yield from t1()
        yield f"t2 end...{value}"


    t = t2()
    # for _ in t:
    #     print(_)
    print(next(t))
    print(next(t))
    print(next(t))
    print(next(t))
    print(t.send("xxxx"))
    # print(t.send("yyyy"))
    # print(next(t))

flag = 11
if flag == 1:
    ...


    def sub_gen():
        yield 1
        yield 2
        return "子生成器的返回值"  # 终止值


    def main_gen():
        # 获取子生成器的返回值
        ret = yield from sub_gen()
        print("子生成器返回值:", ret)  # 在生成器结束时输出
        yield "主生成器继续执行"
        return "最终章"


    # 运行生成器
    gen = main_gen()
    print(next(gen))  # 输出: 1
    print(next(gen))  # 输出: 2
    try:
        next(gen)  # 触发子生成器结束，执行 print("子生成器返回值:", ret)
    except StopIteration as e:
        print("生成器结束")  # 隐式捕获 StopIteration


    # 或者通过生成器表达式完整执行
    def run_generator():
        gen = main_gen()
        result = None
        try:
            while True:
                result = next(gen)
                print("生成器输出:", result)
        except StopIteration as e:
            print("最终返回值:", e.value)  # 获取 StopIteration 的 value 属性


    run_generator()

flag = 11
if flag == 1:
    ...


    def sub_gen():
        x = yield 1
        yield x * 2


    def main_gen():
        result = yield from sub_gen()  # 调用方可直接向 sub_gen 发送值
        print("子生成器返回值:", result)


    gen = main_gen()
    print(next(gen))  # 输出 1
    print(gen.send(10))  # 发送值给 sub_gen，输出 20

flag = 11
if flag == 1:
    ...


    # 传统方式
    def chain_old(iters):
        for it in iters:
            for item in it:
                yield item


    # 使用 yield from
    def chain_new(iters):
        for it in iters:
            yield from it  # 自动遍历子生成器


    list1 = [[3, 3, 5, 6], [7, 7, 70]]
    print(list(chain_old(list1)))
    print(list(chain_new((list1))))

flag = 11
if flag == 1:
    ...
    # 示例：合并多个生成器

    def numbers():
        yield from [1, 2, 3]  # 等价于 for num in [1,2,3]: yield num


    def strings():
        yield from ["a", "b", "c"]


    def combined():
        yield from numbers()
        yield from strings()


    l1 = []
    for item in combined():
        print(item)
        l1.append(item)  # 输出: 1 2 3 a b c
    print(l1)

flag = 11
if flag == 1:
    ...


    def sub_gen():
        yield 1
        yield 2
        return "Done"  # 子生成器返回值

    # for i in sub_gen():
    #     print(i)  #无法获取到生成器的返回值done

    sg = sub_gen()
    try:
        print(next(sg))
        print(next(sg))
        print(next(sg))
        print(next(sg))
    except Exception as e:
        print(e.value)
    finally:
        print("#"*20)

    def delegator():
        result = yield from sub_gen()  # 捕获返回值
        print(f"子生成器返回: {result}")


    list(delegator())  # 输出: [1, 2] 后打印 "子生成器返回: Done"

flag = 11
if flag == 1:
    ...


    def inner_gen():
        yield "Inner 1"
        yield "Inner 2"
        return "Inner Done"  # 返回值会被 middle_gen 捕获


    def middle_gen():
        print("Entering middle_gen")
        result = yield from inner_gen()  # 委托给 inner_gen
        print(f"Middle_gen got return: {result}")
        yield "Middle 1"
        return "Middle Done"


    def outer_gen():
        print("Entering outer_gen")
        result = yield from middle_gen()  # 委托给 middle_gen
        print(f"Outer_gen got return: {result}")
        yield "Outer 1"


    # 驱动生成器
    gen = outer_gen()
    for value in gen:
        print(f"Received: {value}")

flag = 11
if flag == 1:
    ...


    def flatten(nested):
        for item in nested:
            if isinstance(item, list):
                yield from flatten(item)  # 递归委托
            else:
                yield item


    data = [1, [2, [3, 4], 5], 6]
    for num in flatten(data):
        print(num)  # 输出: 1 2 3 4 5 6


flag = 11
if flag == 1:
    ...
    import cProfile


    def my_function():
        # 待测试代码
        pass


    cProfile.run('my_function()')

flag = 1
if flag == 1:
    ...
    with open("example2.txt",encoding="utf-8") as f:
        lines = f.readlines()
    print(f"lines:{lines}")

    def read_file(file):
        with open(file, encoding="utf-8") as f1:
            for line in f1.readlines():
                yield line


    def outer_gen(file):
        yield from read_file(file)

    read_gen = outer_gen("example2.txt")
    print(next(read_gen))











