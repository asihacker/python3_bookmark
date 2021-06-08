#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 17:17
# @Author  : AsiHacker
# @File    : namedtuple自定义数据类型.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from collections import namedtuple

# 用这个工具下面我就可以优雅的表示一个坐标数据
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)  # Point(x=1, y=2)
# 下面我定义一个 facebook 的元数据
FaceBook = namedtuple('FaceBook', ['email', 'password', 'cookies'])
f = FaceBook(email="1523825571@qq.com", password='7758258', cookies='xs=ssss;bd=ssss')
print(f)

# 下面我定义一个 wechat 的元数据,下面这个其实是set集合={}表示，不要理解为什么字典！
wechat = namedtuple('wechat', {'phone', 'password'})
w = wechat(phone=18970084363, password='888888')
print(w)

# rename 的作用是，当你的字段为保留字段的时候，会自动帮助你重新命名
wechat = namedtuple('wechat', {'phone', 'password', 'def'}, rename=True)
print(wechat._fields)

# defaults 可以是 None 或者可迭代的默认值。而且 defaults 从右往左匹配。
# 例如，如果 fieldnames 是 ['x', 'y', 'z'] ，defaults 是 （1，2） ,那么x是需要传入的参数， y 的默认值是 1 ，z 的默认值是 2 。
wechat = namedtuple('wechat', {'phone', 'password'}, defaults={'18970084363', 12})
print(wechat._field_defaults)
print(wechat.mro())  # 类里面的mro表示解析顺序

# module#少用
# type:str
# 如果 module 被定义了，那么 named tuple 的 __module__ 属性会被设为该值。
email = namedtuple('email', {'email'}, defaults={'18970084363@qq.com'}, module=str())
print(email)
