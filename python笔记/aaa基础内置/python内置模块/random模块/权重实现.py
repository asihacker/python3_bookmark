#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/27 00:30
# @Author  : AsiHacker
# @File    : 权重实现.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import random

# 方法1
a = [1, 2, 3]
print(random.choices(a, weights=[0.1, 0.4, 0.5], k=50))


# 方法2
# https://www.cnblogs.com/zywscq/p/5469661.html
def random_weight(weight_data):
    """
    权重
    :param weight_data:
    :return:
    """
    total = sum(weight_data.values())  # 权重求和
    ra = random.uniform(0, total)  # 在0与权重和之前获取一个随机数
    curr_sum = 0
    ret = None
    keys = weight_data.keys()  # 使用Python3.x中的keys
    for k in keys:
        curr_sum += weight_data[k]  # 在遍历中，累加当前权重值
        if ra <= curr_sum:  # 当随机数<=当前权重和时，返回权重key
            ret = k
            break
    return ret


for _ in range(100):
    print(random_weight({1: 10.55, 0: 89.45}))
