# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : enum20240719_1.py
@Time    : 2024/7/19 10:18
@Author  : Echo Wang
'''

from enum import Enum,unique,auto

Season = Enum("Season", ("SUMMER", "SPRING", "WINTER", "AUTUMN"))


class MyColor(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3
    WHITE = 4  # 枚举中值相同时，仅第一个会生效
    BLACK = 4
    # WHITE = 5


# unique 将校验value值是否重复
@unique
class MyColor1(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3
    # WHITE = 4
    BLACK = 4


class MyColor2(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()
    WHITE = auto()
    BLACK = auto()
    # WHITE = 5

'''
class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500
'''
flag = 1
if __name__ == '__main__':
    print(MyColor['BLACK'])
    print(MyColor['WHITE'])
    # print(MyColor(4))
    # print(MyColor['RED'])
    #
    # print(MyColor1.BLACK.value)
    #
    # print(MyColor2.BLACK.value)
    # print(list(HttpStatus))
    # for i in HttpStatus:
    #     print(i,i.value)

    # print(MyColor1(4))
    # print(MyColor1['RED'])
    # print(Season["WINTER"])
    # print(Season(1))
    # print(Season.SUMMER.name)
    # print(Season.SUMMER.value)
    # for i in Season:
    #     print(i)
