#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 14:09
# @Author  : AsiHacker
# @File    : 获取文件信息.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from pathlib import Path

# 获取文件信息
for py_file in Path().glob('*.py'):
    print('Name with extension:', py_file.name)  # 全名
    print('Name only:', py_file.stem)  # 名称
    print('suffix:', py_file.suffix)  # 后缀
    print('info:', py_file.stat())  # 详细信息 st_size 大小 st_atime 最近访问时间 st_mtime 最近修改时间
