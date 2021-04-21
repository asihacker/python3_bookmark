#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 20:50
# @Author  : AsiHacker
# @File    : json path.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
book_dict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
            {"category": "fiction",
             "author": "Herman Melville",
             "title": "Moby Dick",
             "isbn": "0-553-21311-3",
             "price": 8.99
             },
            {"category": "fiction",
             "author": "J. R. R. Tolkien",
             "title": "The Lord of the Rings",
             "isbn": "0-395-19395-8",
             "price": 22.99
             }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}

from jsonpath import jsonpath

print(jsonpath(book_dict, '$..author'))  # 如果取不到返回false
print(jsonpath(book_dict, '$..price'))  # 如果取不到返回false
print(jsonpath(book_dict, '$.store.book.[*].category'))  # 如果取不到返回false
print(jsonpath(book_dict, '$.store.book.[0:2].category'))  # 如果取不到返回false
print(jsonpath(book_dict, '$.store.book.[-2:].category'))  # 如果取不到返回false
# 详细教程请看下面
# https://blog.csdn.net/koflance/article/details/63262484?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control
