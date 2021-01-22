#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 16:09
# @Author  : AsiHacker
# @Site    : 
# @File    : yied_demo.py
# @Software: PyCharm
import threading

test_list = ['jb1', 'jb2', 'jb3']


def get_test(test_list: list):
    for key in test_list:
        yield key  # yield 就是返回，但是她可以记住上次的位置


def read_file():
    block_size = 1024
    with open('南田技术部2020-01费用情况.xls', 'rb') as f:
        block = f.read(block_size)
        if block:
            print(111)
            yield block
        else:
            return block


if __name__ == '__main__':
    tt = get_test(test_list)
    print(next(tt))
    print(next(tt))
    print(next(tt))
    # print(next(tt))
    aa = read_file()
    for key in aa:
        print(key)
