#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 14:32
# @Author  : AsiHacker
# @File    : mongo使用pandas保存csv.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pandas as pd

# 任意的多组列表
a = ["a", "b", "c"]
b = ["d", "e", "f"]
# 字典中的key值即为csv中列名
dataframe = pd.DataFrame({'one_name': a, 'two_name': b})
# 将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("debug.csv", index=False, sep=',')
