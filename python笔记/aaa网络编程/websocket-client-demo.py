#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 19:11
# @Author  : AsiHacker
# @File    : websocket-client-demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import websocket


def on_message(ws, message):
    print(ws)
    print(message)


def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")


websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://fbchat.xyz:8181",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
