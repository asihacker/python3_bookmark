#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 11:56
# @Author  : AsiHacker
# @Site    : 
# @File    : pd-demo.py
# @Software: PyCharm
import pandas as pd

# df = pd.read_excel(r'test.xlsx')
df = pd.DataFrame(pd.read_csv('1111.csv', header=1))
print(df.info)
# df = pd.DataFrame(pd.read_excel('1111.xlsx'))
