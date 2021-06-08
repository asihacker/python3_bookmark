#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 15:50
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import sqlparse

raw = 'select * from foo; select * from bar;'
statements = sqlparse.split(raw)
print(statements)
first = statements[0]
print(sqlparse.format(first, reindent=True, keyword_case='upper'))
parsed = sqlparse.parse('select * from foo')[0]
print(parsed.tokens)
