# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250806-sorted深度学习.py
@Time    : 2025/7/7 14:24
@Author  : Echo Wang
'''

flag = 11
if flag == 1:
    ...
    numbers = [3, 1, 4, 1, 5, 9, 2]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)  # 输出: [1, 1, 2, 3, 4, 5, 9]

    sorted_numbers = sorted(numbers, reverse=True)
    print(sorted_numbers)

flag = 11
if flag == 1:
    ...
    # key 参数接受一个函数，该函数会被应用到每个元素上，然后根据函数的返回值进行排序
    words = ["apples", "banana", "cherry", "date", "data"]
    from functools import partial

    new_sort = partial(sorted, key=len, reverse=True)
    print(new_sort(words))
    # 按字符串长度排序
    print(sorted(words, key=len))  # ['date', 'apples', 'banana', 'cherry']
    print(sorted(words, key=len, reverse=True))  # ['date', 'apples', 'banana', 'cherry']

    # 按第二个字符排序
    print(sorted(words, key=lambda x: x[-1]))  # ['banana', 'date', 'apples', 'cherry']

    # 多级排序：先按长度，再按字母顺序
    print(sorted(words, key=lambda x: (
        len(x), x[-1])))  # ['data', 'date', 'banana', 'apples', 'cherry']
    # 多级排序：先按字母顺序,再按长度
    print(sorted(words, key=lambda x: (
        x[-1], len(x))))  # ['data', 'banana', 'date', 'apples', 'cherry']


    def t1(a=0, b=0, c=0):  # 默认值只能写道结尾部分
        print(a,b,c)
        return a + b + c


    sum1 = partial(t1, 10)
    print(sum1(3, 4))

    sum1 = partial(t1, c=10)
    print(sum1(3, 4))

flag = 11
if flag == 1:
    ...

    print("abccsa".count("c"))
    print("abccsa".count("c", 1, 3))
    # 不区分大小写排序
    mixed_case = ["Apple", "banana", "Cherry", "date"]

    print(sorted(mixed_case, key=lambda x: x.lower()))


    def alpha_count(word: str, letter: str):
        return word.lower().count(letter)


    print(sorted(mixed_case, key=lambda x: alpha_count(x, 'a')))

flag = 11
if flag == 1:
    ...
    # 稳定排序
    data = [('red', 1), ('blue', 1), ('red', 3), ('blue', 2)]
    print(sorted(data, key=lambda x: x[1]))

flag = 11
if flag == 1:
    ...
    # 性能优劣

    # 不好的做法：每次计算都调用两次方法
    words = ["Apple", "banana", "Cherry", "date"]
    sort_w1 = sorted(words, key=lambda x: (x.lower(), x[::-1]))
    import timeit

    print(timeit.timeit(lambda: sort_w1, number=100000))  # 0.006643499999999913


    # 更好的做法：预先计算
    def sort_key(word):
        # return (word.lower(), word[::-1])
        return (word[::-1], word.lower())


    sort_w2 = sorted(words, key=sort_key)
    print(timeit.timeit(lambda: sort_w2, number=100000))  # 0.0065134000000000025
    # print("12213"[::-1])

flag = 11
if flag == 1:
    ...
    students = [
        {'name': 'Alice', 'grade': 'B', 'age': 20},
        {'name': 'Bob', 'grade': 'A', 'age': 19},
        {'name': 'Charlie', 'grade': 'B', 'age': 21}
    ]

    # 按成绩升序，年龄降序
    sorted_students = sorted(students, key=lambda x: (x['grade'], -x['age']))
    from pprint import pprint

    pprint(sorted_students)
    # 输出: [
    #   {'name': 'Bob', 'grade': 'A', 'age': 19},
    #   {'name': 'Charlie', 'grade': 'B', 'age': 21},
    #   {'name': 'Alice', 'grade': 'B', 'age': 20}
    # ]

flag = 11
if flag == 1:
    ...
    # 自定义排序顺序：按优先级排序
    priority_order = {'high': 0, 'medium': 1, 'low': 2}
    tasks = ['low', 'high', 'medium', 'low']
    print(sorted(tasks,
                 key=lambda x: priority_order[x]))  # ['high', 'medium', 'low', 'low']

flag = 11
if flag == 1:
    ...
    from operator import itemgetter, attrgetter

    # 列表元素是元组时
    data = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    print(sorted(data, key=itemgetter(1, 2)))  # 先按第2个元素，再按第3个元素排序


    # 对象属性排序
    class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age


    students = [Student('Alice', 'B', 20), Student('Bob', 'A', 19)]
    print(students)
    print(sorted(students, key=attrgetter('grade', 'age')))
