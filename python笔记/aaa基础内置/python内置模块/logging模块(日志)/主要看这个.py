#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 13:49
# @Author  : AsiHacker
# @Site    : 
# @File    : 主要看这个.py
# @Software: PyCharm
import logging
import time
from logging.handlers import TimedRotatingFileHandler

# 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
# debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

# info : 打印info,warning,error,critical级别的日志,确认一切按预期运行
#
# warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作
#
# error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能
#
# critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s',
    datefmt='%Y-%m-%d'
)
log = logging.getLogger('asi')  # 创建一个名叫asi的日志器
# 下面创建一个处理器，这个处理器可以按照天来记录，还可以限制日志个数
log_file_handler = TimedRotatingFileHandler(filename='asi.log', when="S", interval=1, backupCount=7)
# 把处理器添加到日志器里面
log.addHandler(log_file_handler)
for _ in range(100):
    time.sleep(1)
    log.debug('debug message')
    log.info('info message')
    log.warning('warn message')
    log.error('error message')
    log.critical('critical message')
"""
when：是一个字符串，用于描述滚动周期的基本单位，字符串的值及意义如下：
“S”: Seconds
“M”: Minutes
“H”: Hours
“D”: Days
“W”: Week day (0=Monday)
“midnight”: Roll over at midnight
interval: 滚动周期，单位有when指定，比如：when=’D’,interval=1，表示每天产生一个日志文件；
backupCount: 表示日志文件的保留个数；
"""
