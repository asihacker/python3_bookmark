#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 19:42
# @Author  : AsiHacker
# @File    : 接收信号绑定处理对应的事件.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import signal
import time


def receive_signal(signum, stack):
    """用于接收信号，对signum的值区分信号，实现不同的信号做对应的处理"""
    print('接收的signum', signum)


# 注册处理信号的事件，此处对用户定义信号1、用户定义信号2，绑定事件
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print('我的PID: %s' % os.getpid())

# 开启循环监听信号
while True:
    print('Waiting...')
    time.sleep(3)
