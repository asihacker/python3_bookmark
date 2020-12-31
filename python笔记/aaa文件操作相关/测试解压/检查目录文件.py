#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 14:05
# @Author  : AsiHacker
# @File    : 检查目录文件.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# os 模块中 exists() 用法
import os
from pathlib import Path

print(os.path.exists('path_to_check'))

# pathlib 模块中 exists() 用法
print(Path('directory_path').exists())

# 检查路径是否是目录
os.path.isdir('test_folder')
print(Path('test_folder').is_dir())

# 检查路径是否是文件
os.path.isfile('demo.py')
print(Path('demo.py').is_file())
