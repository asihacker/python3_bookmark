#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import logging

pf = logging.getLogger('test')
pf.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
pf.addHandler(ch)
pf.debug('debug message')
pf.info('info message')
pf.warning('warn message')
pf.error('error message')
pf.critical('critical message')
# https://www.jianshu.com/p/e96be02032f9
