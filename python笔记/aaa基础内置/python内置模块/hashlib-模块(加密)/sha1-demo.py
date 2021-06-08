#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 12:40
# @Author  : AsiHacker
# @File    : sha1-Process启动子进程.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import hashlib

hash2 = hashlib.sha1()  # sha1算法，hashlib很多加密算法
hash2.update(bytes('password', encoding='utf-8'))
print(hash2.hexdigest())
help(hash2)