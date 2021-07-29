#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 14:26
# @Author  : AsiHacker
# @File    : demo.txt.txt-png.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from io import BytesIO

from barcode import EAN13
from barcode.writer import ImageWriter

# 命令行
# python-barcode create "123456789000" outfile -b ean --text "陈俊学"

# Write to a file-like object:
rv = BytesIO()
EAN13(str(100000902922), writer=ImageWriter()).write(rv)

# Or to an actual file:
with open("somefile.jpeg", "wb") as f:
    EAN13("100000011111", writer=ImageWriter()).write(f)
