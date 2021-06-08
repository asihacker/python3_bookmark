#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 12:43
# @Author  : AsiHacker
# @File    : sha224-Process启动子进程.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import hashlib

hash4 = hashlib.sha224()
hash4.update(bytes('password', encoding='utf-8'))
print(hash4.hexdigest())
help(hash4)