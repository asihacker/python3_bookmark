#!/usr/bin/python
# coding=utf-8
# TODO:推导式
a_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
a_list = [key for key in a_dict]
print(a_list)
a_list = [a_dict[key] for key in a_dict]
print(a_list)
a_list = [k for k, v in a_dict.items()]
print(a_list)
b_dict = {k: v for k, v in a_dict.items() if v > 3}
print(b_dict)