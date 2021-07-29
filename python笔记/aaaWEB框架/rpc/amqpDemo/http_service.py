#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 12:02
# @Author  : AsiHacker
# @File    : http_service.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# http.py

import json
from nameko.web.handlers import http


class HttpService:
    name = "http_service"

    @http('GET', '/get/<int:value>')
    def get_method(self, request, value):
        return json.dumps({'value': value})

    @http('POST', '/post')
    def do_post(self, request):
        return u"received: {}".format(request.get_data(as_text=True))
