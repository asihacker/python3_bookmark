#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 23:04
# @Author  : AsiHacker
# @File    : pandas 多个列，行读取方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

import pandas as pd

# loc  iloc 都表示行，一个根据索引 一个根据行号
# df1.loc[0,'age']=25      # 思路：先用loc找到要更改的值，再用赋值（=）的方法实现更换值
# df1.iloc[0,2]=25         # iloc：用索引位置来查找

# 取指定多列
data_train = pd.read_csv('train2.csv')
print(data_train[['Sex', 'Age']])
# 取指定多行
data_train = pd.read_csv('train2.csv')
print(data_train.loc[[0, 1]])
