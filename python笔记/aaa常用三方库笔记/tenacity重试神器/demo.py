#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 09:49
# @Author  : AsiHacker
# @File    : redis常用方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from tenacity import retry, stop_after_attempt, retry_if_exception_type


class CaptchaException(BaseException):
    """

    """


@retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(CaptchaException))
def test(i):
    print(i)
    raise CaptchaException


a = [1, 2, 3, 4]

for k in a:
    try:
        test(k)
    except:
        pass
