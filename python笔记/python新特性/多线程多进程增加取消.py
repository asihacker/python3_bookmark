#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 12:56
# @Author  : AsiHacker
# @File    : 多线程多进程增加取消.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import threading
import time
from concurrent.futures import ThreadPoolExecutor

t = ThreadPoolExecutor(max_workers=10)
LOCK = threading.Lock()


def test():
    time.sleep(1)
    with LOCK:
        print(threading.current_thread().name)


if __name__ == '__main__':
    for _ in range(50):
        t.submit(test)
    t.shutdown(cancel_futures=True)
