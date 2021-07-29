#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:27
# @Author  : AsiHacker
# @File    : 使用JoinableQueue队列.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import multiprocessing
from multiprocessing import Process, JoinableQueue
import time, random, os

c = multiprocessing.Lock


# JoinableQueue 创建可连接的共享进程队列，队列允许队列的消费者通知生产者，队列数据已被成功处理完成。
# 通知过程是使用共享的信号和条件变量来实现的。
# 相对于Queue get 的阻塞来说，效率大大提高。
def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))
        q.task_done()  # 向q.join()发送一次信号,证明一个数据已经被取走了


def producer(name, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (name, i)
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' % (os.getpid(), res))
    q.join()  # 生产完毕，使用此方法进行阻塞，直到队列中所有项目均被处理。


if __name__ == '__main__':
    q = JoinableQueue()
    # 生产者们:即厨师们
    p1 = Process(target=producer, args=('包子', q))
    p2 = Process(target=producer, args=('骨头', q))
    p3 = Process(target=producer, args=('泔水', q))

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c1.daemon = True
    c2.daemon = True

    # 开始
    p_l = [p1, p2, p3, c1, c2]
    for p in p_l:
        p.start()

    p1.join()
    p2.join()
    p3.join()
    print('主')

    # 主进程等--->p1,p2,p3等---->c1,c2
    # p1,p2,p3结束了,证明c1,c2肯定全都收完了p1,p2,p3发到队列的数据
    # 因而c1,c2也没有存在的价值了,不需要继续阻塞在进程中影响主进程了。应该随着主进程的结束而结束,所以设置成守护进程就可以了。
