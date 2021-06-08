#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 18:29
# @Author  : AsiHacker
# @Site    : 
# @File    : asyncio-demo-2.py
# @Software: PyCharm
import re

with open('test', 'r') as f:
    aaa = f.read()

result = re.findall(r'value="(.*?)"', aaa)
print(result)
