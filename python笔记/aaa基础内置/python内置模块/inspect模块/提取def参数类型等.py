#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 21:11
# @Author  : AsiHacker
# @File    : 提取def参数类型等.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from inspect import signature


# https://www.jianshu.com/p/c455650f4adc?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation

def test(a: int, b: str, c: list, d: dict):
    return


if __name__ == '__main__':
    sig = signature(test)
    keys = sig.parameters.keys()
    print(sig, keys, list(keys))

    for name, param in sig.parameters.items():
        print(param.kind)
        if param.kind == param.KEYWORD_ONLY:  # kind表示当前参数类型，KEYWORD_ONLY表示参数只能为关键词
            print(name)
