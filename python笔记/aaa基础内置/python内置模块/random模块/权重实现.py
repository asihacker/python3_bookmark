#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/27 00:30
# @Author  : AsiHacker
# @File    : 权重实现.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import random
from collections import Counter

# 方法1
a = [1, 2, 3]
"""
population：集群。
weights：相对权重。
cum_weights：累加权重。
k：选取次数。
"""
print(Counter(random.choices(a, weights=[10, 20, 70], k=10)))

# print(random.uniform(0, 100))
# 方法2
# https://www.cnblogs.com/zywscq/p/5469661.html
# def random_weight(weight_data):
#     """
#     权重
#     :param weight_data:
#     :return:
#     """
#     total = sum(weight_data.values())  # 权重求和
#     ra = random.uniform(0, total)  # 在0与权重和之前获取一个随机数
#     curr_sum = 0
#     ret = None
#     keys = weight_data.keys()  # 使用Python3.x中的keys
#     for k in keys:
#         curr_sum += weight_data[k]  # 在遍历中，累加当前权重值
#         if ra <= curr_sum:  # 当随机数<=当前权重和时，返回权重key
#             ret = k
#             break
#     return ret
#
#
# for _ in range(20):
#     print(random_weight({1: 1 - 0.1, 2: 1 - 0.5, 3: 1 - 0.7, 4: 0.4}))
