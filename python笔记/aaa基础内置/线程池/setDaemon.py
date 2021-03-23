#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/23 13:13
# @Author  : AsiHacker
# @File    : setDaemon.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(5)
        print("This is " + self.getName())


if __name__ == "__main__":
    t1 = MyThread(999)
    t1.setDaemon(True)  # 设置这个子线程的守护进程为主线程，那么主线程退出后，子线程不会执行
    t1.start()
    print("I am the father thread.")
