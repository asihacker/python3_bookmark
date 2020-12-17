#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 14:35
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
# 主要函数
# timeit(stmt=’pass’, setup=’pass’, timer=<defaulttimer>, number=1000000)
# 返回：
#
# 返回执行stmt这段代码number遍所用的时间，单位为秒，float型
#
# 参数：
#
# stmt：要执行的那段代码
#
# setup：执行代码的准备工作，不计入时间，一般是import之类的
#
# timer：这个在win32下是time.clock()，linux下是time.time()，默认的，不用管
#
# number：要执行stmt多少遍
#
# repeat(stmt=’pass’, setup=’pass’, timer=<defaulttimer>, repeat=3, number=1000000)
# 这个函数比timeit函数多了一个repeat参数而已，表示重复执行timeit这个过程多少遍，返回一个列表，表示执行每遍的时间
import timeit


def test(num):
    _ = [k for k in range(num)]
    return


def test2(num):
    _ = list()
    for k in range(num):
        _.append(k)
    return


if __name__ == '__main__':
    print(timeit.timeit(stmt="[k for k in range(10)]"))
