#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 12:41
# @Author  : AsiHacker
# @File    : sha256-Process启动子进程.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import hashlib

hash3 = hashlib.sha256()  # 不同算法，hashlib很多加密算法
hash3.update(bytes('password', encoding='utf-8'))
print(hash3.hexdigest())
help(hash3)
