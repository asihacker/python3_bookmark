# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 19:49
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from jazzit import error_track


@error_track("curb_your_enthusiasm.mp3", wait=7)
def run():
    for num in reversed(range(10)):
        print(10 / num)


if __name__ == "__main__":
    run()
