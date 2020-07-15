#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 23:31
# @Author  : AsiHacker
# @Site    : 
# @File    : demo2.py
# @Software: PyCharm
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 23:28
# @Author  : AsiHacker
# @Site    :
# @File    : demo.py
# @Software: PyCharm
import asyncio
import threading


async def washing1(content: str):
    await asyncio.sleep(1)
    print(threading.current_thread().name, 'washing1')
    return content


async def washing2(content: str):
    await asyncio.sleep(2)
    print(threading.current_thread().name, 'washing2')
    return content


async def washing3(content: str):
    await asyncio.sleep(3)
    print(threading.current_thread().name, 'washing3')
    return content


def task_callback(task):
    print(task.result())


# async def strat():
#     await washing1()
#     await washing2()
#     await washing3()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    task1 = asyncio.ensure_future(washing1('washing1'))
    task2 = asyncio.ensure_future(washing2('washing2'))
    task3 = asyncio.ensure_future(washing3('washing3'))

    tasks = [
        task1, task2, task3
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    loop.close()
    pass
