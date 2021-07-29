# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 15:35
# @Author  : AsiHacker
# @File    : whatlangid库实现
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from whatlangid import WhatLangId
wtl = WhatLangId()
print(wtl.predict_lang("昆明武科大扭矩"))
print(wtl.predict_pro(["English sentence", "അമ്മ"]))