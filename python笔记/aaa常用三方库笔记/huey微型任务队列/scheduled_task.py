#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 20:29
# @Author  : AsiHacker
# @File    : scheduled_task.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

from task import add_numbers

# 延时任务
res = add_numbers.schedule((2, 3), delay=5)  # Will be run in ~10s.
print(res(blocking=True))  # Will block until task finishes, in ~10s.
