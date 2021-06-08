#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:27
# @Author  : AsiHacker
# @File    : __class__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from python笔记.aaa基础内置.类相关.抽象类定义 import C

obj = C()
print(obj.__module__)  # 输出 lib.aa，即：输出模块
print(obj.__class__)  # 输出 lib.aa.C，即：输出类
