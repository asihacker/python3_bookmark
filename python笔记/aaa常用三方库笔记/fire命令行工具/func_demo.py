#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 11:39
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import fire


def hello(name="World"):
    return "Hello %s!" % name


if __name__ == '__main__':
    fire.Fire(hello)
