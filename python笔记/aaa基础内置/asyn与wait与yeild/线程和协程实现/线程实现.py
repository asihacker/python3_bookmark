#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 19:40
# @Author  : AsiHacker
# @Site    : 
# @File    : 线程实现.py
# @Software: PyCharm
import time
from concurrent.futures import ThreadPoolExecutor
import requests
import threading

lock = threading.Lock()
# lock.release()

def add():
    rsp = requests.get("http://www.baidu.com")
    lock.acquire()
    print(threading.currentThread().getName(), rsp.status_code)
    lock.release()
    return


if __name__ == '__main__':
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=10) as t:
        for _ in range(100):
            t.submit(add).done()
    print(time.time() - t0)
