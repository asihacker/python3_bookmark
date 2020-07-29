#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 13:08
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
from faker import Faker

# 使用教程 https://www.jianshu.com/p/6bd6869631d9
f = Faker(locale='zh_CN')
for _ in range(10):
    print(f.profile())
