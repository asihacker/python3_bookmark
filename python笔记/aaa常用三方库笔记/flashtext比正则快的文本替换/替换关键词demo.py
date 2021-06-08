#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:41
# @Author  : AsiHacker
# @File    : 替换关键词demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from flashtext import KeywordProcessor
# 1. 初始化关键字处理器, 注意设置大小写敏感(case_sensitive)为TRUE
# keyword_processor = KeywordProcessor(case_sensitive=True)
# 1. 初始化关键字处理器
keyword_processor = KeywordProcessor()
# 2. 添加关键词
keyword_processor.add_keyword('New Delhi', 'NCR region')
# 3. 替换关键词
new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.new delhi｜new delhi｜new delhi')
# 4. 结果
print(new_sentence)