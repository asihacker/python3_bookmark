#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 18:33
# @Author  : AsiHacker
# @File    : demo.py
# @Software: PyCharm
import json

data = {'a': 1, 'b': 2}
print(json.dumps(data, separators=(',', ':')))
print(json.dumps(data))
