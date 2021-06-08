#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 14:46
# @Author  : AsiHacker
# @Site    : 
# @File    : 1创建主窗口大小位置标题.py
# @Software: PyCharm


def test1(data: str):
    """
    测试断言
    :param bet:
    :return:
    """
    assert 'wxid' in data, '错误互加data'  # 用于内部检测参数是否符合要求
    return data


if __name__ == '__main__':
    print(test1('wxid——12313123'))
    raise Exception('123')
    # a = 123
    # raise KeyError('fuck')
