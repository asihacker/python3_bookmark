#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 12:16
# @Author  : AsiHacker
# @File    : 抽象类定义.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from abc import ABC, abstractmethod


class C(ABC):
    @abstractmethod
    def my_abstract_method(self):
        ...

    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls):
        ...

    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod():
        ...

    @property
    @abstractmethod
    def my_abstract_property(self):
        ...

    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val):
        ...

    @abstractmethod
    def _get_x(self):
        ...

    @abstractmethod
    def _set_x(self, val):
        ...

    x = property(_get_x, _set_x)
