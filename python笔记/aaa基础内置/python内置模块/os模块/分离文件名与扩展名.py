#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 17:18
# @Author  : AsiHacker
# @File    : 分离文件名与扩展名.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os

path_01 = 'E:\STH\Foobar2000\install.log'
path_02 = 'E:\STH\Foobar2000'
res_01 = os.path.splitext(path_01)
res_02 = os.path.splitext(path_02)
print(res_01)
print(res_02)