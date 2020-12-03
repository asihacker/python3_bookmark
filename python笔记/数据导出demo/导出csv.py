#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 21:36
# @Author  : AsiHacker
# @Site    : 
# @File    : 导出csv.py
# @Software: PyCharm
import csv

mydict = {'key1': 'value_a', 'key2': 'value_b', 'key3': 'value_c'}
f = open('dict.csv', 'w')
w = csv.DictWriter(f, mydict.keys())
w.writerow(mydict)
f.close()
