#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 10:09
# @Author  : AsiHacker
# @File    : asyncio-demo.txt.txt-1.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

from birdseye import eye


@eye
def foo(a: int = 10):
    b = a + 10
    return b


if __name__ == '__main__':
    foo()
