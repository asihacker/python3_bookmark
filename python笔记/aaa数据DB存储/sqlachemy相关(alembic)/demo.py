#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 23:53
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm
import os
import sys

print(os.path.dirname(os.path.abspath(__file__)) + "/../")
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(sys.path.append(os.getcwd()))