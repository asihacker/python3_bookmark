#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 23:40
# @Author  : AsiHacker
# @File    : singledispatch-泛型函数.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from functools import singledispatch


# 可以实现根据一个函数入参类型的不一样，来走不同的逻辑

@singledispatch
def fun(text):
    print('String：' + text)


@fun.register(int)
def _(text):
    print(text)


@fun.register(list)
def _(text):
    for k, v in enumerate(text):
        print(k, v)


@fun.register(float)
@fun.register(tuple)
def _(text):
    print('float, tuple')


fun('i am is hubo')
fun(123)
fun(['a', 'b', 'c'])
fun(1.23)
print(fun.registry)  # 所有的泛型函数
print(fun.registry[int])  # 获取int的泛型函数

# 下面是泛型函数装饰器的某个用途，处理json.dump下面的未知数据类型

import json
from datetime import datetime, date

now = datetime.now()
d = {'now': now, 'name': 'XiaoMing'}


# print(json.dumps(d))#直接这样会报错
def json_encoder(obj):
    """
    未知类型dump处理
    :param obj:
    :return:
    """
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError(f'{repr(obj)} is not JSON serializable')


print(json.dumps(d, default=json_encoder))
