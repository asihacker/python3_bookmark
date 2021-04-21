#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 23:10
# @Author  : AsiHacker
# @File    : pandas增 删 查 改.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import datetime
import pandas as pd

loc = "./football/"
s_time = '2021/1/1'
e_time = '2021/4/10'
s_time, e_time = map(lambda x: datetime.datetime.strptime(x, '%Y/%m/%d'), [s_time, e_time])
raw_data = pd.read_csv('胜负平.csv')
raw_data['time'] = pd.to_datetime(raw_data['time'], format='%Y-%m-%d %H:%M')  # 把某列时间转化为时间格式
raw_data = raw_data.loc[
    ((raw_data.odds_31 <= 1.5) | (raw_data.odds_33 <= 1.5)) &
    (raw_data.time >= s_time) & (raw_data.time <= e_time)
    ]  # 条件查询
print(raw_data)
