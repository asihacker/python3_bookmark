#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 14:19
# @Author  : AsiHacker
# @Site    : 
# @File    : 重试.py
# @Software: PyCharm
# https://www.jianshu.com/p/f68342acecc4 教程地址
from tenacity import retry, stop_after_attempt, retry_if_result, retry_if_exception_type


def is_ok(value):
    """
    重试辅助方法
    :param value:
    :return:
    """
    return value is None


def return_last_value(retry_state):
    """return the result of the last call attempt"""
    return retry_state.outcome.result()  # 表示返回原函数的返回值


a = lambda value: value is None


@retry(
    retry=retry_if_result(lambda value: value is None),
    stop=stop_after_attempt(3),
    retry_error_callback=lambda retry_state: retry_state.outcome.result()
)
def test(a: int, ccc):
    print(next(ccc))
    # assert a > 0, 'fuck'
    if a < 0:
        return None
    return a


def dddd():
    for key in range(100):
        yield key


if __name__ == '__main__':
    ccc = dddd()
    print(test(-11, ccc))
