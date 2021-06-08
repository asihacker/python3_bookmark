#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 16:10
# @Author  : AsiHacker
# @File    : Condition锁.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

import threading, time


def Seeker(cond, name):
    time.sleep(2)
    cond.acquire()
    print('%s :我已经把眼睛蒙上了！' % name)
    cond.notify()
    cond.wait()
    for i in range(3):
        print('%s is finding!!!' % name)
        time.sleep(2)
    cond.notify()
    cond.release()
    print('%s :我赢了！' % name)


def Hider(cond, name):
    cond.acquire()
    cond.wait()
    for i in range(2):
        print('%s is hiding!!!' % name)
        time.sleep(3)
    print('%s :我已经藏好了，你快来找我吧！' % name)
    cond.notify()
    cond.wait()
    cond.release()
    print('%s :被你找到了，唉~^~!' % name)


if __name__ == '__main__':
    cond = threading.Condition()
    seeker = threading.Thread(target=Seeker, args=(cond, 'seeker'))
    hider = threading.Thread(target=Hider, args=(cond, 'hider'))
    seeker.start()
    hider.start()
# 执行结果：
# seeker :我已经把眼睛蒙上了！
# hider is hiding!!!
# hider is hiding!!!
# hider :我已经藏好了，你快来找我吧！
# seeker is finding!!!
# seeker is finding!!!
# seeker is finding!!!
# seeker :我赢了！
# hider :被你找到了，唉~^~!
