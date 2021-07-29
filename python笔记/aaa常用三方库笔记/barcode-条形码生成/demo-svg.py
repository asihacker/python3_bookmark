#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 14:23
# @Author  : AsiHacker
# @File    : demo.txt.txt-svg.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from io import BytesIO

from barcode import EAN13
from barcode.writer import SVGWriter

# Write to a file-like object:
rv = BytesIO()
EAN13(str("100000902922"), writer=SVGWriter()).write(rv)

# Or to an actual file:
with open("somefile.svg", "wb") as f:
    EAN13(str(100000011111), writer=SVGWriter()).write(f)
