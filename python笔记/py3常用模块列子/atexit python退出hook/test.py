#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 14:18
# @Author  : AsiHacker
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import atexit


def clear_task_2():
    print('清理任务2')


@atexit.register
def clear_task():
    print('清理任务')


if __name__ == '__main__':
    1 / 0
