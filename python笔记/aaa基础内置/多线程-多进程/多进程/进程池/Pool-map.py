#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:33
# @Author  : AsiHacker
# @File    : Pool-map.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os
from multiprocessing import Pool
import time


def task(i):
    i += 1
    time.sleep(1)
    return f'{os.getppid()}>>>{os.getpid()}>>>{i}'


if __name__ == '__main__':
    '''
    分配进程个数时，推荐建议使用cpu核数+1
    '''
    # 方法一
    # start = time.time()
    # p = Pool(5)  # 相当于实例化了 5 个进程
    # p.map(task, range(200))  # 相当于 p.start()  ,天生异步，每次执行5个进程
    #
    # p.close()  # 为了防止继续往里面提交任务，保护进程池，关闭掉进程池所接收的任务通道
    # p.join()  # 等待子进程执行完毕
    #
    # print(time.time() - start)  # 计算开启进程所消耗的总时间
    # 方法二
    start = time.time()
    with Pool(processes=5) as P:
        c = P.map(task, range(50))
    print(c)
    print(time.time() - start)  # 计算开启进程所消耗的总时间
