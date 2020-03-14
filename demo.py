#!/usr/bin/python
# coding=utf-8
import random


class dog(object):
    def __init__(self):
        self.name = ''.join(random.sample('zxcvbnasdfgh', 10))

    def __str__(self):
        return self.name


a = dog()
print(str(a))
