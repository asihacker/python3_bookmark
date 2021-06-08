#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:16
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import nltk
# nltk.download('punkt')
# nltk.download('words')
from nltk.corpus import treebank

# sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
sentence = """我今天学习了一个新的框架，我很开心。"""
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)
entities = nltk.chunk.ne_chunk(tagged)
print(entities)
# t = treebank.parsed_sents('wsj_0001.mrg')[0]
# t.draw()
