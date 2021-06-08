#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 18:33
# @Author  : AsiHacker
# @File    : 自定义异常.py
# @Software: PyCharm
import json

data = {'bet': 1, 'b': 2}
print(json.dumps(data, separators=(',', ':')))
print(json.dumps(data))