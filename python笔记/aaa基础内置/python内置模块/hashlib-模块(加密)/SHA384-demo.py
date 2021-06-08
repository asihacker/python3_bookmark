#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 12:43
# @Author  : AsiHacker
# @File    : SHA384-Process启动子进程.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import hashlib

hash5 = hashlib.sha384()  # 不同算法，hashlib很多加密算法
hash5.update(bytes('password', encoding='utf-8'))
print(hash5.hexdigest())
help(hash5)
