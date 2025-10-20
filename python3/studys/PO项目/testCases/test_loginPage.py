# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : test_loginPage.py
@Time    : 2025/7/9 14:16
@Author  : Echo Wang
'''

import pytest, pytest_assume


# 多重断言 用pytest.assume

def test_01():
    # a, b = 1, 2
    # assert a == b
    assert 2 == 3


def test_02():
    # pytest.assume(1 == 2)
    assert 2 == 4


def test_03():
    a, b = 1, 2
    with pytest_assume: assert a == b
    assert 2 == 4


if __name__ == '__main__':
    # pytest.main(['-sv', '-k', '02', __file__])
    pytest.main(['-sv', __file__])
