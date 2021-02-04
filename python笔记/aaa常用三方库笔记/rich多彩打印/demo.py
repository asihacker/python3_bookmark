#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 10:05
# @Author  : AsiHacker
# @File    : redis常用方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os
import sys

from rich import print
from rich.columns import Columns

directory = os.listdir(sys.argv[1])
print(Columns(directory))