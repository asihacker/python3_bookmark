#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:46
# @Author  : AsiHacker
# @File    : 批量添加关键词dict.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from flashtext import KeywordProcessor

# 1. 初始化关键字处理器
keyword_processor = KeywordProcessor()
# 2. （第一种）通过字典批量添加关键词,其实就是添加key对应的value，其中value需要是str_list
keyword_dict = {
    "java": ["java_2e", "java programing"],
    "product management": ["PM", "product manager"]
}
keyword_processor.add_keywords_from_dict(keyword_dict)
# 2. （第二种）通过数组批量添加关键词
# keyword_processor.add_keywords_from_list(["java", "python"])
# 3. 第一种的提取效果如下
keywords_found = keyword_processor.extract_keywords('I am a product manager for a java_2e platform PM', span_info=True)
print(keywords_found)
# output ['product management', 'java']
