#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 10:19
# @Author  : AsiHacker
# @File    : redis常用方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# import PythonMagick
#
# img = PythonMagick.Image('统计.jpg')
# # 这里要设置一下尺寸，不然会报ico尺寸异常错误
# img.sample('128x128')
# img.write('统计.ico')
from PIL import Image
from PIL import Image

img = Image.open('统计.png')
# icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
icon_sizes = [(64, 64)]
img.save('统计.ico', sizes=icon_sizes)

