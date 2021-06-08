#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 23:25
# @Author  : AsiHacker
# @File    : box-getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from box import Box

# pip install python-box
my_box = Box(key="value")
print(my_box.key)  # value

my_box = Box({"team": {"red": {"leader": "Sarge", "members": []}}})
print(my_box.team.red.leader)  # Sarge
my_box.team.red.members = [
    {"name": "Grif", "rank": "Minor Junior Private Negative First Class"},
    {"name": "Dick Simmons", "rank": "Captain"}
]
print(my_box.team.red.members[0].name)  # Grif
