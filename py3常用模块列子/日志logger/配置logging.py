#!/usr/bin/python
# coding=utf-8
import datetime
import logging
import time
from logging.handlers import TimedRotatingFileHandler

# logging.basicConfig(
#     filename=f'{datetime.datetime.now().strftime("%H:%M:%S")}test.log',
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
#     datefmt='%Y-%m-%d'
# )
log = logging.getLogger('asi')
log_file_handler = TimedRotatingFileHandler(filename='asi', when="S", interval=1, backupCount=7)
log.addHandler(log_file_handler)

"""
format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
"""
for _ in range(100):
    time.sleep(1)
    log.info('test info')
    log.debug('test debug')
    log.warning('test warning')
    log.error('test error')
    log.critical('test critical')
    log.info('44444')
