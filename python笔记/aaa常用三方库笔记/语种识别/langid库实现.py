#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 12:32
# @Author  : AsiHacker
# @Site    : 
# @File    : langid库实现.py
# @Software: PyCharm
import re
import time

import langid


def remove_noise(document):
    noise_pattern = re.compile("|".join(["http\S+", "\@\w+", "\#\w+"]))
    clean_text = re.sub(noise_pattern, "", document)
    return clean_text

test = """
hi
Hi~
現在不方便接聽現在不方便接聽現在不方便接聽
昆明武科大扭矩
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
        t0 = time.perf_counter()
        print(langid.classify(t))
        print(time.perf_counter() - t0)
