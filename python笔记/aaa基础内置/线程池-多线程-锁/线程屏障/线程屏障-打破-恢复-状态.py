#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 18:28
# @Author  : AsiHacker
# @File    : 线程屏障-打破-恢复-状态.py.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import threading, logging

logging.basicConfig(level=logging.INFO, format="[-] %(threadName)s %(message)s")

def work(barrier: threading.Barrier):
    logging.info("n_waiting = {}".format(barrier.n_waiting))
    try:
        bid = barrier.wait()
        logging.info("after barrier {}".format(bid))
    except threading.BrokenBarrierError:
        logging.info("Broken Barrier in {}".format(threading.current_thread()))


barrier = threading.Barrier(3)

for x in range(1, 12):  # 12个
    print("屏障状态", barrier.broken)
    if x == 3:
        threading.get_ident()
        barrier.abort()  # 打破屏障
    elif x == 6:
        barrier.reset()  # 恢复屏障
    threading.Event().wait(1)
    threading.Thread(target=work, args=(barrier,), name="Barrier-{}".format(x)).start()

# broken  检测栅栏是否处于打破的状态，返回True或False
#
# abort()  将栅栏置于broken状态，等待中的线程或者调用等待方法的线程都会抛出threading.BrokenBarrieError异常，直到reset方法来恢复栅栏
#
# reset()  恢复屏障，重新开始拦截
