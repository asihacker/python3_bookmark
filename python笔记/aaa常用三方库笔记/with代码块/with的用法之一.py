#!/usr/bin/python
# coding=utf-8
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import requests


def index(url):
    print(threading.current_thread().getName())
    r = requests.get(url)
    return r.status_code


with ThreadPoolExecutor(10) as t:
    t.map(index, ["https://www.baidu.com" for _ in range(50)])

with ThreadPoolExecutor(max_workers=20, thread_name_prefix='asi') as t:
    obj_list = []
    for page in range(50):
        obj = t.submit(index, "https://www.baidu.com")
        obj_list.append(obj)
    for future in as_completed(obj_list):
        data = future.result()
        print(f"main: {data}")
print(123)
# with open('../自动安装py包/requirements.txt', 'r') as f:
#     content = ''.join([key.replace('/n', '/r/n').rjust(40, '*') for key in f.readlines()])
#     print(content)
