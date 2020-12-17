#!/usr/bin/python
# coding=utf-8
import threading

if __name__ == '__main__':
    event_id = threading.Event()
    print('事件id', event_id)
    threading.Timer(1, function=lambda event_id: event_id.set(), args=[event_id]).start()
    print(event_id.wait(3))
    print('事件结束')
