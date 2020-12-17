#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:27
# @Author  : AsiHacker
# @File    : __class__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from lib.aa import C

obj = C()
print(obj.__module__)  # 输出 lib.aa，即：输出模块
print(obj.__class__)  # 输出 lib.aa.C，即：输出类
