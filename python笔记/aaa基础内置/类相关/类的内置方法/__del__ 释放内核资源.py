#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 18:29
# @Author  : AsiHacker
# @File    : __del__ 释放内核资源.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 注：如果产生的对象仅仅只是python程序级别的（用户级），那么无需定义__del__,如果产生的对象的同时还会向操作系统发起系统调用，即一个对象有用户级与内核级两种资源，比如（打开一个文件，创建一个数据库链接），则必须在清除对象的同时回收系统资源，这就用到了__del__
f = open('bet.txt')  # 做了两件事，在用户空间拿到一个f变量，在操作系统内核空间打开一个文件
del f  # 只回收用户空间的f，操作系统的文件还处于打开状态

# 所以我们应该在del f之前保证f.close()执行,即便是没有del，程序执行完毕也会自动del清理资源，于是文件操作的正确用法应该是
f = open('bet.txt')
# 读写...
f.close()
# 很多情况下大家都容易忽略f.close, 这就用到了with上下文管理
