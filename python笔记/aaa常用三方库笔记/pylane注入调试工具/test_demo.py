#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 21:08
# @Author  : AsiHacker
# @File    : test_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os
import sys
import time


def test1():
    print(sys._getframe().f_code.co_name)


def test2():
    print(sys._getframe().f_code.co_name)


if __name__ == '__main__':
    print(os.getpid())
    while 1:
        time.sleep(1)