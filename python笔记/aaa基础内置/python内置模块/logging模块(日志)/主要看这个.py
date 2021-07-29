#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 13:49
# @Author  : AsiHacker
# @Site    : 
# @File    : 主要看这个.py
# @Software: PyCharm
import logging
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

"""
format
%(levelno)s	打印日志级别的数值
%(levelname)s	打印日志级别名称
%(pathname)s	打印当前执行程序的路径
%(filename)s	打印当前执行程序名称
%(funcName)s	打印日志的当前函数
%(lineno)d	打印日志的当前行号
%(asctime)s	打印日志的时间
%(thread)d	打印线程id
%(threadName)s	打印线程名称
%(process)d	打印进程ID
%(message)s	打印日志信息
"""
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s',
    datefmt='%Y-%m-%d'
)
log = logging.getLogger('asi')  # 创建一个名叫asi的日志器
# 下面创建一个处理器，这个处理器可以按照天来记录，还可以限制日志个数
"""
处理器
 
StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
FileHandler：logging.FileHandler；日志输出到文件
BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件
SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址
SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器
"""
log_file_handler = TimedRotatingFileHandler(filename='asi.log', when="M", interval=2, backupCount=7)
"""
RotatingHandler 参数
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

# 把处理器添加到日志器里面
log.addHandler(log_file_handler)
a = {'a': 1, 'b': 3}
log.debug(a)
log.debug('debug message')
log.info('info message')
log.warning('warn message')
log.error('error message')
log.critical('critical message')
log.critical(exc_info=Exception('123'), msg='123')
