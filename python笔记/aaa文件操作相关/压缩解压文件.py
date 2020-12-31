#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 14:14
# @Author  : AsiHacker
# @File    : 压缩解压文件.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from pathlib import Path
from zipfile import ZipFile

# 创建压缩文件
with ZipFile('text_files.zip', 'w') as file:
    for txt_file in Path().glob('*.py'):
        print(f"*添加文件: {txt_file.name} 到压缩文件")
        file.write(txt_file)

# 解压缩文件
with ZipFile('text_files.zip') as zip_file:
    zip_file.printdir()
    zip_file.extractall('测试解压')
    # zip_file.extract('测试解压')
