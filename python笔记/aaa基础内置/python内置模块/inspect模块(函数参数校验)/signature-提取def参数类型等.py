#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 21:11
# @Author  : AsiHacker
# @File    : signature-提取def参数类型等.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from inspect import signature
from inspect import Parameter


# https://www.jianshu.com/p/c455650f4adc?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation

def test(a: int, b: str, *, c: list, d: dict, e: int = 10, f=990,g=None):  # *号表示后面的参数变为关键词参数
    return


if __name__ == '__main__':
    sig = signature(test)
    # keys = sig.parameters.keys()
    # print(sig, keys, list(keys))

    for name, param in sig.parameters.items():
        print(name, param.name, param.annotation, param.kind, param.default, param.empty)
        if param.default == Parameter.empty:
            print('没有默认值')
        # print(param.annotation)
        # print(param)
# POSITIONAL_ONLY  - 只能是位置参数
# POSITIONAL_OR_KEYWORD - 位置参数或者关键词参数
# VAR_POSITIONAL - 可选位置参数，对应*args
# VAR_KEYWORD - 可选关键词参数，对应**kwargs
