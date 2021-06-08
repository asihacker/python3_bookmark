#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 19:17
# @Author  : AsiHacker
# @File    : json dumps default.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
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
