#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 22:08
# @Author  : AsiHacker
# @File    : asyncio-demo-2.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import logging
import time

from decorator import decorator


@decorator
def warn_slow(func, time_limit=60, *args, **kw):
    t0 = time.time()
    result = func(*args, **kw)
    dt = time.time() - t0
    if dt > time_limit:
        print('%s took %d seconds', func.__name__, dt)
    else:
        print('%s took %d seconds', func.__name__, dt)
    return result


@warn_slow(time_limit=600)  # warn if it takes more than 10 minutes
def run_calculation(tempdir, outdir):
    pass


if __name__ == '__main__':
    run_calculation(1, 2)
