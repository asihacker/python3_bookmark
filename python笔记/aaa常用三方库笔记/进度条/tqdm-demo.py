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

jdt = tqdm(range(100))

# for i in jdt:
#     jdt.set_description(f"{os.path.abspath(__file__)}")
#     sleep(0.01)
# jdt.set_description(f"{os.getcwd()}")
for i in jdt:
    # jdt.set_description(f"{os.getcwd()}")
    sleep(0.01)

# from tqdm.notebook import trange
#
# for i in trange(10):
#     sleep(0.01)
