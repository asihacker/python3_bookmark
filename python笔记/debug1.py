#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 17:26
# @Author  : AsiHacker
# @File    : debug1.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import datetime


def format_time(source_list: list):
    """
    格式化时间
    :param source_list:
    :return:
    """
    _ = str(datetime.datetime.now().year) + '-' + ' '.join(source_list[0])
    hour = 24 if 'p' in _ else 12
    return datetime.datetime.strptime(_.replace('p', ':00').replace('a', ':00'),
                                      '%Y-%m-%d %H:%M:%S') + datetime.timedelta(
        hours=hour)


if __name__ == '__main__':
    # a = format_time([('03-10', '03:00a')])
    # print(str(a),type(a))
    dd = [1, 7, 8, 2, 3, 4, 5, 5, 5, 5]
    aa = {'name': 123}
    # del dd[10]
    print(dd.index(3))
    print(dd.count(5))
    print(dd.extend(range(100)))
    print(dd.sort(reverse=True))
    # del aa['name']
    print(aa.setdefault('age', 123))
    print(aa.popitem())
    print(aa.popitem())
    print(dd)
    print(aa)
    import sys

    print(sys.getrecursionlimit())
