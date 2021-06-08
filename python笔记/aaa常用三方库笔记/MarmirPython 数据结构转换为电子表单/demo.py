#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 15:54
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

import datetime
import mm

# $ pip install Marmir


now = datetime.datetime.now().replace(microsecond=0)

my_data = [
    {
        'msg': "My first Row",
        'id': 1,
        'when': now,
    },
    {
        'msg': "My second Row",
        'id': 2,
        'when': now,
    },

]
# mm_doc = mm.Document(my_data)
mm_doc = mm.Date(my_data)
mm_doc.write("example.xls")
