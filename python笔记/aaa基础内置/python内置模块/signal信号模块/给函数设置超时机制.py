#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 19:08
# @Author  : AsiHacker
# @File    : 给函数设置超时机制.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import signal
import time


# 信号只能工作在主线程!!!!!!!
# 自定义超时异常
class TimeoutError(Exception):
    def __init__(self, msg):
        super(TimeoutError, self).__init__()
        self.msg = msg


def time_out(interval, callback):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError("run func timeout")

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)  # interval秒后向进程发送SIGALRM信号
                result = func(*args, **kwargs)
                signal.alarm(0)  # 函数在规定时间执行完后关闭alarm闹钟
                return result
            except TimeoutError as e:
                callback(e)

        return wrapper

    return decorator


def timeout_callback(e):
    print(e.msg)


@time_out(2, timeout_callback)
def task1():
    print("task1 start")
    time.sleep(3)
    print("task1 end")


@time_out(2, timeout_callback)
def task2():
    print("task2 start")
    time.sleep(1)
    print("task2 end")


if __name__ == "__main__":
    # 信号只能工作在主线程
    # threading.Thread(target=task1).start()
    # threading.Thread(target=task2).start()
    task1()
    task2()
