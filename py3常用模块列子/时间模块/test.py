#!/usr/bin/python
# coding=utf-8
import datetime
import time

# %a 英文星期简写
# %A 英文星期的完全
# %b 英文月份的简写
# %B 英文月份的完全
# %c 显示本地日期时间
# %d 日期，取1-31
# %H 小时， 0-23
# %I 小时， 0-12
# %m 月， 01 -12
# %M 分钟，1-59
# %j 年中当天的天数
# %w 显示今天是星期几
# %W 第几周
# %x 当天日期
# %X 本地的当天时间
# %y 年份 00-99间
# %Y 年份的完整拼写

yz_time = '2018-09-23 23:30:21'
print(time.strptime(yz_time, '%Y-%m-%d %H:%M:%S'))
# 时间增减
aaa = datetime.datetime.strptime(yz_time, '%Y-%m-%d %H:%M:%S')
b = datetime.timedelta(days=7)
print(type(aaa), aaa, b, aaa + b)

str_now_time = time.strftime('%Y-%m-%d %H:%M:%S')
print(time.strptime(str_now_time, '%Y-%m-%d %H:%M:%S'))
