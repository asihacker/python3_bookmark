#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 12:43
# @Author  : AsiHacker
# @File    : SHA512-Process启动子进程.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import hashlib

hash6 = hashlib.sha512()  # 不同算法，hashlib很多加密算法
hash6.update(bytes('password', encoding='utf-8'))
print(hash6.hexdigest())
help(hash6)
