#!/usr/bin/python
# coding=utf-8
import nsq
import tornado.ioloop
import time


def pub_message():
    writer.pub('asi_debug', time.strftime('%H:%M:%S').encode('utf-8'), finish_pub)


def finish_pub(conn, data):
    print(conn,data)


# writer = nsq.Writer(['nsq.fqwang.net:4150'])
writer = nsq.Writer(['39.100.77.40:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
