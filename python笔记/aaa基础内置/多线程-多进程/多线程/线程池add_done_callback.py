#!/usr/bin/python
# coding=utf-8
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def add_num(a):
    time.sleep(random.randint(1, 2))
    return f'{threading.current_thread().getName()}=>{a + random.randint(1, 10)}'


def parse(obj):
    print(f'回调结果：{obj.result()}')
    return


with ThreadPoolExecutor(max_workers=50, thread_name_prefix='asi') as executor:
    for key in range(250):
        executor.submit(add_num, 1).add_done_callback(parse)  # 提交线程池处理数据,设置线程回调
print('全部执行完毕！')
