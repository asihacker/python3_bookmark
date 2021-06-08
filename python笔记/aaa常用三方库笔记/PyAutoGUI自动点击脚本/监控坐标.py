#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 11:11
# @Author  : AsiHacker
# @File    : 监控坐标.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pyautogui as pag

try:
    while True:
        a = '%4d,%4d'%pag.position()
        print(a)
except Exception as e:
    print(e)