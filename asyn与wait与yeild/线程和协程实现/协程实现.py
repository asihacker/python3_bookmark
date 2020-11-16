#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 19:46
# @Author  : AsiHacker
# @Site    : 
# @File    : 协程实现.py
# @Software: PyCharm
import asyncio
import time

import requests


async def add():
    await requests.get("http://www.baidu.com")
    return


if __name__ == '__main__':
    t0 = time.time()
    loop = asyncio.get_event_loop()
    task_list = [asyncio.ensure_future(add) for _ in range(100)]
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()
    print(time.time() - t0)
