#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 14:50
# @Author  : AsiHacker
# @File    : 字典点式操作列子.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
class Dict(dict):
    """
    demo
    """

    def __init__(self, *args, **kwargs):
        super(Dict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        return self.get(key)

    def __setattr__(self, key, value):
        self[key] = value


a = {'data': {'name': 'asi', 'age': 18}}
c = Dict(a)
print(c.data)
