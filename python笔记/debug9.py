#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 20:06
# @Author  : AsiHacker
# @File    : debug9.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import marshmallow

from marshmallow.fields import *
import marshmallow as ma
from inspect import signature

print(ma.Schema.TYPE_MAPPING)


class Test1(ma.Schema):
    a = ma.fields.String()
    b = ma.fields.Int()



import datetime as dt
import uuid


def test(a: str, b: int, c: dt.datetime, d: uuid.UUID):
    print(a, b)


sig = signature(test)
for k, v in sig.parameters.items():
    print(ma.Schema.TYPE_MAPPING.get(v.annotation))

print(String)
print(Int)
# Test2 = type('_', (ma.Schema,), {k: v.annotation for k, v in sig.parameters.items()})

t1 = Test1()
t2 = ma.Schema.from_dict(
    {"a": String(), "b": Int()}
)()
print(t1.load({'a': 'asi', 'b': '123'}))
print(t2.load({'a': 'asi', 'b': '123'}))

#
