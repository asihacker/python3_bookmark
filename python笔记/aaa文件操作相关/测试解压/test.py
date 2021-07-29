#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 16:53
# @Author  : AsiHacker
# @File    : debug.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os

for k in os.walk(os.path.dirname(__file__), topdown=True, onerror=None, followlinks=False):
    print(k)
