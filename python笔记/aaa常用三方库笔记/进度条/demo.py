#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 09:38
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
from __future__ import absolute_import

import os
from time import sleep
from tqdm import tqdm
jdt = tqdm(range(1000))

# for i in jdt:
#     jdt.set_description(f"{os.path.abspath(__file__)}")
#     sleep(0.01)
for i in jdt:
    jdt.set_description(f"{os.getcwd()}")
    sleep(0.01)
