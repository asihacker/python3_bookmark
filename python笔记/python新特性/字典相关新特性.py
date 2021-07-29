#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 11:34
# @Author  : AsiHacker
# @File    : 字典相关新特性.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.


a: str = '10'  # 字符串
b: float = 2.33  # 小数
c: int = 2  # 整数
# 集合～～～～那就是 Python 内置类型 dict，list ，tuple 是线程安全的
d: list[int] = [1, 2, '3']  # 有序
e: set = {1, 2, 3}  # 无序不重复
f: tuple = (1, 2, 3)  # 有序 创建不可修改
g: dict = {'bet': 1, 'b': 2, 'c': 3}  # 字典
primes: list[int] = [1, 2.88, '3']


def test(bet: list[int]) -> list[int, str]:
    """
    123123123
    :param bet: 123213
    :return:
    """
    return bet + [1]


if __name__ == '__main__':
    t: list[int] = [1, 2, 3, 3]
    if (y := len(t)) > 3:
        print('xx')
    print(y)

    cc: dict[str:int] = {'a': 1, 'b': 2, 'c': 3}
    dd: dict[str:int] = {'a': 2, 'b': 6, 'c': 3, 'd': 4}
    aa = cc | dd
    print(aa, cc, dd)
    # cc.update(dd)
    # print(cc)
    # print({**cc, **dd})
    cc |= dd
    print(dd, cc)
    eee = range(4)
    for k in eee:
        print(k)
