# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 19:39
# @Author  : AsiHacker
# @File    : 使用退出上下文
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import contextlib


def callback():
    print('B')


with contextlib.ExitStack() as stack:
    stack.callback(callback)

    print('A')
