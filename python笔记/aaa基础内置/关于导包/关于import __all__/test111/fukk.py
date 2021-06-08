#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 16:17
# @Author  : AsiHacker
# @Site    : 
# @File    : fukk.py
# @Software: PyCharm
import inspect
import sys


def test_h1():
    print(sys._getframe().f_code.co_name)
    return


def test_h2():
    print(sys._getframe().f_code.co_name)
    print(sys._getframe().f_back.f_lineno)  # 获取行号
    return


if __name__ == '__main__':
    test_h2()
