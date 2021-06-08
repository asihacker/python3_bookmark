#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 20:17
# @Author  : AsiHacker
# @File    : func_demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from attr import attrs, attrib
from cattr import structure, unstructure


@attrs
class User(object):
    name = attrib()
    age = attrib()


data = {
    'name': 'Germey',
    'age': 23
}
user = structure(data, User)
print('user', user)
json = unstructure(user)
print('json', json)
