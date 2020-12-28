#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 20:08
# @Author  : AsiHacker
# @File    : run_task.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

from task import add_numbers
#普通任务
res = add_numbers(1, 2)
print(res.id, res.get(blocking=True))