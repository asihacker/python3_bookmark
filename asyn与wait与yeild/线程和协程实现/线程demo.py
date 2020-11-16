#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 19:40
# @Author  : AsiHacker
# @Site    : 
# @File    : 线程demo.py
# @Software: PyCharm
import time
from concurrent.futures import ThreadPoolExecutor
import requests
import threading


def add():
    rsp = requests.get("http://www.baidu.com")
    # print(threading.currentThread().getName(), rsp.status_code)
    return


if __name__ == '__main__':
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=10) as t:
        for _ in range(100):
            t.submit(fn=add).done()
    print(time.time() - t0)
