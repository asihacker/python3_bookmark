#!/usr/bin/python
# coding=utf-8
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flask_demo import config
from flask_demo.test_blue import index_page

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
CORS(app, supports_credentials=True)  # 设置跨域
app.register_blueprint(index_page, url_prefix='/index')  # 注册蓝图
#
# from app import app
# from .admin import admin
# from .user import user
# #这里分别给app注册了两个蓝图admin,user
# #参数url_prefix='/xxx'的意思是设置request.url中的url前缀，
# #即当request.url是以/admin或者/user的情况下才会通过注册的蓝图的视图方法处理请求并返回
# app.register_blueprint(admin,url_prefix='/admin')
# app.register_blueprint(user, url_prefix='/user')
