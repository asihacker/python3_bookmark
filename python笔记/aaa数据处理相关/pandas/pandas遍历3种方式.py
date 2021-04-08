#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 23:06
# @Author  : AsiHacker
# @File    : pandas遍历3种方式.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# iterrows(): 按行遍历，将DataFrame的每一行迭代为(index, Series)对，可以通过row[name]对元素进行访问。
# itertuples(): 按行遍历，将DataFrame的每一行迭代为元祖，可以通过row[name]对元素进行访问，比iterrows()效率高。
# iteritems():按列遍历，将DataFrame的每一列迭代为(列名, Series)对，可以通过row[index]对元素进行访问。
# raw_data.loc[li[0], '结果'] = 1 : 更新数据
