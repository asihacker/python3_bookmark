#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 21:41
# @Author  : AsiHacker
# @File    : demo.txt.txt.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time

from deepface import DeepFace

t0 = time.perf_counter()
for k in range(100000):
    obj = DeepFace.analyze(img_path="1.jpg", actions=['age', 'gender'], enforce_detection=False)
    print(obj["age"], " years old ", obj["gender"])
t1 = time.perf_counter()
print("耗费时间", t1 - t0)
