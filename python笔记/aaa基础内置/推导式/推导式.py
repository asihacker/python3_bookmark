#!/usr/bin/python
# coding=utf-8
# TODO:推导式
a = [i for i in range(10) if i % 2 == 0]
print(a)
a = [i if i % 2 == 0 else 'qi' for i in range(10)]
print(a)
# a_dict = {'bet': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# a_list = [key for key in a_dict]
# print(a_list)
# a_list = [a_dict[key] for key in a_dict]
# print(a_list)
# a_list = [k for k, v in a_dict.items()]
# print(a_list)
# b_dict = {k: v for k, v in a_dict.items() if v > 3}
# print(b_dict)
import time

a = list()
t0 = time.time()
for k in range(100000000):
    a.append(k)
print(time.time() - t0)
t0 = time.time()
a = [key for key in range(100000000)]
print(time.time() - t0)
