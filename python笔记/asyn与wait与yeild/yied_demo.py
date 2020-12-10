#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 16:09
# @Author  : AsiHacker
# @Site    : 
# @File    : yied_demo.py
# @Software: PyCharm
import threading

aa = [2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 9, 0]
# print(aa.index(9))
# aa.reverse()
# aa.sort()
# print(aa)
# bb = [*aa]
# bb=aa
bb = aa.copy()
# breakpoint()
print(id(aa))
print(id(bb))


def test2(n):
    for i in range(n):
        yield i


def sttt():
    for i in test2(50):
        print(i)


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
    # threading.Thread(target=sttt).start()
    aa = read_file()
    for key in aa:
        print(key)

    # b=bytearray()
    #
    # b.extend(x)
    # for x in aa:
    #     print(x)

    pass
# def get_content(entry):
#     for block in entry.get_blocks():
#         yield block
# def get_content(entry):
#     yield from entry.get_blocks()
