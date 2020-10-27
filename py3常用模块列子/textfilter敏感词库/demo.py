#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 14:43
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
from filter import DFAFilter

gfw = DFAFilter()
gfw.parse("keywords")
print("待过滤：售假人民币 我操操操")
print("过滤后：", gfw.filter("售假人民币 我操操操", "*"))
