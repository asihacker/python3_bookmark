#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 13:15
# @Author  : AsiHacker
# @File    : demo.txt.txt-svg.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import qrcode

# * error_ correction:控制二维码纠错级别。
#
# * ERROR_ CORRECT_ _L:大约7%或者更少的错误会被更正。
#
# * ERROR_ CORRECT_ _M:默认值，大约15%或者更少的错误会被更正。
#
# * ERROR_ CORRECT_ Q:大约25%或者更少的错误会被更正。
#
# * ERROR_ CORRECT_ H:大约30%或者更少的错误会被更正。
#
# * box_ size: 控制二维码中每个格子的像素数，默认为10。
#
# * border:控制二维码四周留白包含的格子数，默认为4。
#
# * image_ factory: 选择生成图片的形式，默认为PIL图像。
#
# * mask_ pattern: 选择生成图片的的掩模。


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.cnblogs.com/nthforsth/p/12290779.html')
qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save('7788.ico')
