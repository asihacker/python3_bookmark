#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 10:57
# @Author  : AsiHacker
# @File    : 创建目录.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# print(os.mkdir("test_folder"))#存在会报错，需要先判断目录是否存在，这种方式是不安全的，它会导致竞争条件。
import os
from pathlib import Path

try:
    print(os.mkdir("test_folder"))  # 存在会报错，需要先判断目录是否存在，这种方式是不安全的，它会导致竞争条件。
except Exception as err:
    print(err)
print(Path("test_folder").mkdir(parents=True, exist_ok=True))  # 推荐使用这个
# parents：如果父目录不存在，是否创建父目录。
# exist_ok：只有在目录不存在时创建目录，目录已存在时不会抛出异常。
print(Path("tmp_level0/tmp_level1").mkdir(parents=True, exist_ok=True))

try:
    print(os.makedirs('tmp_level0/tmp_level1'))
except Exception as err:
    print(err)
