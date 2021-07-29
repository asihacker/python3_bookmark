#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:38
# @Author  : AsiHacker
# @File    : 提取关键词demo.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from flashtext import KeywordProcessor

# 1. 初始化关键字处理器
keyword_processor = KeywordProcessor()
# 2. 添加关键词
keyword_processor.add_keyword('Big Apple', 'New York')  # 第一个参数代表需要被查找的关键词，第二个参数是给这个关键词一个别名，如果找到了则以别名显示。
keyword_processor.add_keyword('Bay Area')
keyword_processor.add_keyword('love')
# 3. 处理目标句子并提取相应关键词 span_info=True 标记关键词位置
keywords_found = keyword_processor.extract_keywords('I love Big Apple and Bay Area.love love love', span_info=True)
# 4. 结果
print(keywords_found)
# ['New York', 'Bay Area']
print(keyword_processor.get_all_keywords())
