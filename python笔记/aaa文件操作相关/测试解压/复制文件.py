#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 14:02
# @Author  : AsiHacker
# @File    : 复制文件.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import shutil
from pathlib import Path

source_file = "test_folder/hello.txt"
target_file = "hello2.txt"
target_file_path = Path(target_file)
print("* 复制前，文件存在:", target_file_path.exists())
shutil.copy(source_file, target_file)
print("* 复制后，文件存在:", target_file_path.exists())
