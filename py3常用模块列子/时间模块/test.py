#!/usr/bin/python
# coding=utf-8
import datetime
import time

yz_time = '2018-09-23 23:30:21'
print(time.strptime(yz_time, '%Y-%m-%d %H:%M:%S'))

aaa = datetime.datetime.strptime(yz_time, '%Y-%m-%d %H:%M:%S')
b = datetime.timedelta(days=7)
print(type(aaa), aaa, b, aaa + b)
