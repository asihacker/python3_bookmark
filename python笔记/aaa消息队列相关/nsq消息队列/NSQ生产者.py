import nsq
import tornado.ioloop
import time


def pub_message():
    writer.pub('order', time.strftime('%H:%M:%S').encode(), finish_pub)


def finish_pub(conn, data):
    print(data)


writer = nsq.Writer(['fbchat.xyz:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
