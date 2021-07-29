# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 09:37
# @Author  : AsiHacker
# @File    : fastlangid
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from fastlangid.langid import LID
langid = LID()
result = langid.predict('This is a test')
print(result)
