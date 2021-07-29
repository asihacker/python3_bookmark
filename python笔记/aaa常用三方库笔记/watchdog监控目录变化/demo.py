#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 16:11
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# -*- coding: utf-8 -*-
# 作用: 用于监控目录的变化,调用对应的处理逻辑

import time

from watchdog.events import *
from watchdog.observers import Observer

# 设置系统编码格式

# 创建一个logger，设置日志
logger = logging.getLogger('MonitorDir')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('testLog.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter(
    '[%(asctime)s] [%(thread)d] [%(filename)s] [line: %(lineno)d][%(levelname)s] ## %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)


class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        if event.is_directory:
            logger.info("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            logger.info("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            logger.info("directory created:{0}".format(event.src_path))
        else:
            logger.info("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            logger.info("directory deleted:{0}".format(event.src_path))
        else:
            logger.info("file deleted:{0}".format(event.src_path))

    # 主要监控目录下有文件修改
    def on_modified(self, event):
        # 监控目录下面的目录
        if event.is_directory:
            logger.info("directory modified:{0}".format(event.src_path))
        else:
            logger.info("file modified:{0}".format(event.src_path))


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    # 监控目录
    observer.schedule(event_handler, "debug", True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:  # 在某种情况下，要避免ctrl+c突然终止进程导致python报错，可以捕获KeyboardInterrupt 这个异常来进行对应处理
        print('123123')
        observer.stop()
    observer.join()
