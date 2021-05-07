#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 20:20
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import datetime as dt
import time

# https://blog.csdn.net/yutu75/article/details/110457378
from marshmallow import Schema, fields

"""
fields.String(*, default, missing, data_key, …) 字符串类型

fields.UUID(*, default, missing, data_key, …) UUID字符串类型

fields.Integer(*, strict, **kwargs) 整数类型

fields.Decimal(places, rounding, *, allow_nan, …) 支持Python中的decimal类型，常用语金额类字段

fields.Boolean(*, truthy, falsy, **kwargs) 布尔类型

fields.Float(*, allow_nan, as_string, **kwargs) 浮点类型

fields.DateTime(format, **kwargs) 日期时间类型

fields.Date(format, **kwargs) 日期类型

fields.Email(*args, **kwargs) 邮箱字符串类型

fields.List(cls_or_instance, type], **kwargs) 列表类型，常用于接收数组数据

fields.Dict(keys, type] = None, values, …) 字典类型，常用于接收json类型数据
————————————————
版权声明：本文为CSDN博主「haeasringnar」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/haeasringnar/article/details/109339949
"""


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.created_at = dt.datetime.now()
        self.created_at = int(time.time())

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    # created_at = fields.DateTime()
    created_at = fields.Integer()


user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
print(result)
