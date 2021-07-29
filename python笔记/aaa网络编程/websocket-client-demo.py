#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 19:11
# @Author  : AsiHacker
# @File    : websocket-client-task.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import websocket


# https://github.com/websocket-client/websocket-client

def on_message(ws, message):
    print(ws)
    print(message)
    ws.close(status=1011, reason=b'qowome')
    # ws.send('1111111111111111111111111111111111'.encode('utf-8'), opcode=websocket.ABNF.OPCODE_BINARY)


def on_error(ws, error):
    print(ws)
    print(error)


def on_ping(ws, *args, **kwargs):
    print(args, kwargs)
    print("### ping ###")


def on_pong(ws, message):
    print(message)
    print("### pong ###")


def on_open(ws, *args):
    print(ws, args)
    ws.send('你好'.encode('utf-8'), opcode=websocket.ABNF.OPCODE_BINARY)


def on_close(ws, close_status_code, close_msg):
    # Because on_close was triggered, we know the opcode = 8
    print("on_close args:")
    if close_status_code or close_msg:
        print("close status code: " + str(close_status_code))
        print("close message: " + str(close_msg))


websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://127.0.0.1:9898",
                            on_message=on_message,
                            on_error=on_error,
                            on_ping=on_ping,
                            on_pong=on_error,
                            on_open=on_open,
                            on_close=on_close)

# ws.run_forever(http_proxy_host='127.0.0.1', http_proxy_port=1086)
ws.run_forever()
