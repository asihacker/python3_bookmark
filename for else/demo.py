#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 11:58
# @Author  : AsiHacker
# @Site    : 
# @File    : demo.py
# @Software: PyCharm


def check(item, item_list):
    """

    :param item:
    :param item_list:
    :return:
    """
    for key in item_list:
        if item == key:
            print('存在哦')
            break
    else:
        print('不存在')


if __name__ == '__main__':
    check('a', ['a', 'b', 'c'])
