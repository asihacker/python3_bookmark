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

    # x = property(_get_x, _set_x)


class D(C):

    def my_abstract_method(self):
        pass

    @classmethod
    def my_abstract_classmethod(cls):
        pass

    @staticmethod
    def my_abstract_staticmethod():
        pass

    def _get_x(self):
        pass

    def _set_x(self, val):
        pass

    @property
    def my_abstract_property(self):
        pass


# control + I 快速实现接口
if __name__ == '__main__':
    aaa = D()
