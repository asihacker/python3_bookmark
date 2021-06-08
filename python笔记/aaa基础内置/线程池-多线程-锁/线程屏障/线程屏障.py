#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 18:24
# @Author  : AsiHacker
# @File    : 线程屏障.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import threading, logging
import time

logging.basicConfig(level=logging.INFO, format="[-] %(threadName)s %(message)s")


def work(barrier: threading.Barrier):
    logging.info("n_waiting = {}".format(barrier.n_waiting))  # 等待的线程数
    bid = barrier.wait()  # 线程屏障
    logging.info("after barrier {}".format(bid))  # 屏障之后

barrier = threading.Barrier(3)  # 3个参与者，每3个开闸放行，0,1,2  4,5,6

for x in range(1, 4):  # 所有参数者个数，4,5,6,10,15
    threading.Event().wait(1)  # 这里用time.sleep(1)一样
    threading.Thread(target=work, args=(barrier,), name="Barrier-{}".format(x)).start()
