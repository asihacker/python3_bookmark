# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 19:52
# @Author  : AsiHacker
# @File    : demo
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import pandas as pd
from pandasgui import show

df = pd.DataFrame(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
show(df)
