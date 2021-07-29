#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 17:56
# @Author  : AsiHacker
# @File    : 重入锁Rlock.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# ①原始锁，原始锁是一个
# ②在锁定时不属于特定线程的同步基元组件
# ③acquire()/release() 对可以嵌套，重入锁必须由获取它的线程释放。一旦线程获得了重入锁，同一个线程再次获取它将不阻塞。
# import threading
#
# rlock = threading.RLock()
#
#
# def func():
#     if rlock.acquire():  # 第一把锁
#         print(threading.currentThread().getName(), "first lock")
#         if rlock.acquire():  # 第一把锁没解开的情况下接着上第二把锁
#             print(threading.currentThread().getName(), "second lock")
#             rlock.release()  # 解开第二把锁
#         rlock.release()  # 解开第一把锁
#
#
# t = threading.Thread(target=func)
# t2 = threading.Thread(target=func)
# t.start()
# t2.start()
import threading

lock1 = threading.RLock()#使用重入锁则完美解决
# lock1 = threading.Lock()  # 这里使用这个会导致死锁

def inner():
    with lock1:  # 使用with自动 锁定和释放！！！！好用
        print("inner1 function:%s" % threading.current_thread())


def outer():
    print("outer function:%s" % threading.current_thread())
    with lock1:  # 使用with自动 锁定和释放！！！！好用
        inner()


if __name__ == "__main__":
    t1 = threading.Thread(target=outer)
    t1.start()
