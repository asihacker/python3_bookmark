#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 17:20
# @Author  : AsiHacker
# @File    : redis常用方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import datetime

from freezegun import freeze_time  # pip install freezegun


@freeze_time("2012-01-14")
def test():
    print(datetime.datetime.now())
    assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)


if __name__ == '__main__':
    test()
