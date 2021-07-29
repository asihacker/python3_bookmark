#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 16:38
# @Author  : AsiHacker
# @File    : socket-io-client.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import os
import eventlet
from eventlet import wsgi

os.environ['EVENTLET_HUB'] = 'poll'  # python3.9需要设置poll
eventlet.monkey_patch()
import socketio

# !!!python3.9请设置环境变量 EVENTLET_HUB=poll
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid, environ)
    sio.emit('my_message', data=f'hello,{sid}', to=sid)
    return True


@sio.event
def my_message(sid, data):
    print('message ', data)
    sio.emit('my_message', data='fuck', to=sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
