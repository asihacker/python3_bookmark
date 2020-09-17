#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 12:07
# @Author  : AsiHacker
# @Site    : 
# @File    : dataclass模块.py
# @Software: PyCharm
import yaml

# 教程 https://www.cnblogs.com/klb561/p/9326677.html
# 写出
aproject = {'name': 'Silenthand Olleander',
            'race': 'Human',
            'traits': ['ONE_HAND', 'ONE_EYE']
            }

with open('test.yml', 'w+') as f:
    f.write(yaml.dump(aproject))
# 读取
with open('test.yml', 'r') as f:
    print(yaml.full_load(f.buffer))
