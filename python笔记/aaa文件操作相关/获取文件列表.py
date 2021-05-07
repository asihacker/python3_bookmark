#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 11:13
# @Author  : AsiHacker
# @File    : 获取文件列表.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from pathlib import Path
from glob import glob

# txt_files = list(Path('./tmp_level0').glob("*py"))
# print(txt_files)
files = list(glob('*py'))
print(files)

