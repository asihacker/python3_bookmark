#!/usr/bin/python
# coding=utf-8
import threading
import time

event_id = 1
event_list = {}
content_list = {}


def add(x, y):
    print(threading.current_thread().getName())
    list = [key for key in range(100000)]
    return x * y


def add2(x, y):
    print(threading.current_thread())  # 获取线程名称id
    a = list()
    for key in range(100000):
        a.append(a)
    return x * y


def creat_event_id():
    global event_id
    event_id += 1
    event = threading.Event()  # 创建一个事件
    event_list[event_id] = event
    return event_id


def set_content(eid, val, set_time):
    time.sleep(set_time)
    global event_list
    global content_list
    content_list[eid] = val
    event = event_list[eid]
    event.set()  # 事件触发
    return


def get_event_id_content(event_id):
    global event_list
    global content_list
    event = event_list[eid]
    event.wait(15)  # 事件等待
    return content_list.get(event_id)


if __name__ == '__main__':
    eid = creat_event_id()
    threading.Thread(target=set_content, args=[eid, '1hahahah', 6]).start()
    threading.Timer(3, function=print, args=[111111, 111]).start()  # 启动线程后多少秒执行
    print(333)
    print(get_event_id_content(eid))
    print('ok')

# threading.Thread(target=add, args=[1, 1]).start()
# threading.Thread(target=add2, args=[1, 1]).start()
# print(threading.active_count())  # 打印当前活动线程数
# print(threading.activeCount())  # 打印当前活动线程数
# print(threading.enumerate())  # 打印当前活动线程列表
