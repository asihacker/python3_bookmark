#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import logging

# 创建一个Logger 记录器
pf = logging.getLogger('test')
pf.setLevel(logging.DEBUG)
# 创建一个Handler 处理器 写入日志到文件
# fh = logging.FileHandler('atp43.log')
# # 设置日志等级
# fh.setLevel(logging.DEBUG)
# 创建一个Handler 处理器 写入日志到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
# pf.addHandler(fh)
pf.addHandler(ch)
# 记录一条日志
pf.debug('debug message')
pf.info('info message')
pf.warning('warn message')
pf.error('error message')
pf.critical('critical message')
# https://www.jianshu.com/p/e96be02032f9
