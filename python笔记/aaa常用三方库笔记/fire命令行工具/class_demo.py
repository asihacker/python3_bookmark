#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 11:40
# @Author  : AsiHacker
# @File    : class_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import fire


class Calculator(object):
    """A simple calculator class."""

    def double(self, number):
        return 2 * number


if __name__ == '__main__':
    fire.Fire(Calculator)
