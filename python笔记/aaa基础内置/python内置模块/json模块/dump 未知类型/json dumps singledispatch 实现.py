#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 19:23
# @Author  : AsiHacker
# @File    : json dumps singledispatch 实现.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import json
from datetime import datetime, date
from functools import singledispatch

now = datetime.now()
d = {'now': now, 'name': 'XiaoMing'}


@singledispatch
def json_encoder(obj):
    raise TypeError(f'{repr(obj)} is not JSON serializable')


@json_encoder.register(date)
@json_encoder.register(datetime)
def encode_date_time(obj):
    return obj.isoformat()


print(json.dumps(d, default=json_encoder))
