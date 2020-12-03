#!/usr/bin/python
# coding=utf-8
import nsq
import tornado.ioloop
import time


def pub_message():
    a = time.strftime()
    writer.pub('test', a, finish_pub)


def finish_pub(conn, data):
    print(conn, data)


writer = nsq.Writer(['127.0.0.1:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 1).start()
nsq.run()
