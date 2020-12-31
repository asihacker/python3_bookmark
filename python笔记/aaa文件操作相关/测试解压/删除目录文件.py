#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 11:00
# @Author  : AsiHacker
# @File    : 删除目录文件.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os

with open('tmp.txt', 'w') as f:
    f.write('123')

print(os.remove('tmp.txt'))
print(os.rmdir('test_folder'))
