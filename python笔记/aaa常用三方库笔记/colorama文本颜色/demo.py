#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 10:10
# @Author  : AsiHacker
# @File    : findall.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from colorama import Fore, Back, Style, init

"""
Fore 字体颜色 ：
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET

Back 字体背景色：
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET

Style 字体格式：
DIM, NORMAL, BRIGHT, RESET_ALL

作者：星塵子
链接：https://www.jianshu.com/p/f8cf7fb4525e
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
print(Fore.RED + 'some red text')
print(Back.BLACK + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')