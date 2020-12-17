#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 16:52
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm
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
