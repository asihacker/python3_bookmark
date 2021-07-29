#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 20:05
# @Author  : AsiHacker
# @File    : 查找项目根目录.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

# 把上级目录加入 PATH 中
import inspect
import os
import sys

cur_dir = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
dir = os.path.dirname(cur_dir)
print(dir)
# sys.path.append(dir)
print(sys.path)

import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
# 添加apps目录
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))