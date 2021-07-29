#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 16:38
# @Author  : AsiHacker
# @File    : socket-io-client.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')
    sio.emit('my_message', 'word')
    return True

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my_message', 'word')
    sio.send({'response': 'my response'})
    print(sio.transport())


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:5000')
sio.wait()
