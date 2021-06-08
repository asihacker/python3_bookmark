#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 15:34
# @Author  : AsiHacker
# @File    : getframeinfo-谁调用了我.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import phonenumbers

# https://github.com/daviddrysdale/python-phonenumbers
X = phonenumbers.parse("+8618970084363", None)
print(phonenumbers.format_number(X, phonenumbers.PhoneNumberFormat.NATIONAL))
print(phonenumbers.format_number(X, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(X, phonenumbers.PhoneNumberFormat.E164))
