#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import logging

logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')
# create a log file
logger = logging.getLogger('atp_log')
logger.setLevel(logging.DEBUG)
# create a handler, write the log info into it
fh = logging.FileHandler('atp.log')
fh.setLevel(logging.DEBUG)
# create another handler output the log though console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
# 记录一条日志
logger.info('foorbar')
logger.error('foorbar')
#https://www.jianshu.com/p/e96be02032f9