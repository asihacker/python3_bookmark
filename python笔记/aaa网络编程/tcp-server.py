#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 17:40
# @Author  : AsiHacker
# @File    : tcp-server.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from socket import *
from time import ctime

host = ''
port = 8081
buffsize = 2048
ADDR = (host, port)

tctime = socket(AF_INET, SOCK_STREAM)
tctime.bind(ADDR)
tctime.listen(3)

while True:
    print('Wait for connection ...')
    tctimeClient, addr = tctime.accept()
    print("Connection from :", addr)

    while True:
        data = tctimeClient.recv(buffsize).decode()
        if not data:
            break
        tctimeClient.send(('[%s] %s' % (ctime(), data)).encode())
    tctimeClient.close()
# tctimeClient.close()
