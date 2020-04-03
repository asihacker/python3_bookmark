#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import logging

# 创建一个Logger 记录器
pf = logging.getLogger('test')
gl = logging.Filter(name='err')
pf.setLevel(logging.DEBUG)
# 创建一个Handler 处理器 写入日志到控制台
ch = logging.StreamHandler()
# 设置日志等级
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
"""
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
formatter = logging.Formatter(
    '%(lineno)d - %(name)s - %(asctime)s - %(levelname)s - %(funcName)s - %(threadName)s - %(message)s')

ch.setFormatter(formatter)
# 给logger添加handler
pf.addHandler(ch)

# 记录一条日志
pf.debug('debug message')
pf.info('info message')
pf.warning('warn message')
pf.error('error message')
pf.critical('critical message')
# https://www.jianshu.com/p/e96be02032f9
