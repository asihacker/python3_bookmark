#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 10:49
# @Author  : AsiHacker
# @File    : imap.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import itertools

# TODO:待查原因为啥imap没啦
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):  # 貌似没有这个方法啦～～～
    print(x)
