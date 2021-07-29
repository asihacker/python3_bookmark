#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 15:10
# @Author  : AsiHacker
# @File    : charset_normalizer库实现.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import time

from charset_normalizer import detect

test = """
陈俊学陈俊学
现在不方便接听。
現在不方便接聽。
It is not convenient to answer the call now.
今すぐ電話に出るのは不便です。
지금 전화를받는 것은 편리하지 않습니다.
अभी कॉल का उत्तर देना सुविधाजनक नहीं है।
Tidak nyaman untuk menjawab panggilan sekarang.
atau pihak berkuasa tempatan berkaitan larangan lawatan yang mungkin memberi kesan kepada anda
"""

if __name__ == '__main__':
    a = list(filter(lambda x: x != '', test.split('\n')))
    for t in a:
        print(t)
        # print(detect(t))
        # t0 = time.perf_counter()
        print(detect(t.encode()))
        # print(time.perf_counter() - t0)
