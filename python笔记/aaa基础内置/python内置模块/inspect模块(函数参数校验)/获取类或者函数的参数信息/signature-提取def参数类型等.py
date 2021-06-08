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

def test(a: int, b: str, *, c: list, d: dict, e: int = 10, f=990, g=None):  # *号表示后面的参数变为关键词参数
    return


def test2(a: int, b: str, /, c: list, d: dict, e: int = 10, *, f=990, g=None):  # /号表示前面为位置参数
    return


ParameterKind = [
    {"POSITIONAL_OR_KEYWORD": "可以通过定位参数和关键字参数传入的形参, python函数的参数多数属于此类"},  # 普通参数
    {"VAR_POSITIONAL": "定位参数元组"},  # *args
    {"VAR_KEYWORD": "关键字参数字典"},  # **kwargs
    {"KEYWORD_ONLY": "仅限关键字参数"},  # 类似于 下边d=100 的这种
    {"POSITIONAL_ONLY": "仅限定位参数, python声名的函数不支持, 但是有些c语言实现且不接受关键字参数的函数, 例如: divmod 支持"},
]

if __name__ == '__main__':
    sig = signature(test2)
    # keys = sig.parameters.keys()
    # print(sig, keys, list(keys))

    for name, param in sig.parameters.items():
        print(name, param.name, param.annotation, param.kind, param.default, param.empty)
        if param.default == Parameter.empty:
            ...
        #     print('没有默认值')
        # print(param.annotation)
        # print(param)
# POSITIONAL_ONLY  - 只能是位置参数
# POSITIONAL_OR_KEYWORD - 位置参数或者关键词参数
# VAR_POSITIONAL - 可选位置参数，对应*args
# VAR_KEYWORD - 可选关键词参数，对应**kwargs

    from inspect import Signature, Parameter

    # 创建一个函数参数列表，列表内的元素由类Parameter的实例组成
    # Parameter实例化时，依次接受参数名、参数类型、默认值和参数注解
    # 默认值和参数类型默认为空，这里的空值不是None，而是Parameter.empty，代表没有值
    params = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
              Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=9),
              Parameter('z', Parameter.VAR_KEYWORD)]

    # 使用Signature类，接受函数参数列表，实例化出函数签名实例
    sig = Signature(params)
    print(sig)
