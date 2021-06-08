#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 09:55
# @Author  : AsiHacker
# @File    : print-输出到文件.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
with open('test.log', mode='w+') as f:
    print('123123', file=f)
