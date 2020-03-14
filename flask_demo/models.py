#!/usr/bin/python
# coding=utf-8
import datetime
import random
import string
import time

from flask_demo import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, comment='自增ID')
    pid = db.Column(db.Integer, unique=True, autoincrement=True)  # 自动递增
    name = db.Column(db.String(32), index=True, unique=True, comment='用户姓名')
    age = db.Column(db.Integer, nullable=False, default=18, comment='年龄')
    sign = db.Column(db.Text, comment='用户签名')
    email = db.Column(db.String(128), unique=True, index=True, comment='邮件')
    time = db.Column(db.DateTime, default=datetime.datetime.now, index=True, comment='创建时间')


def get_random_text(cnt: int = 1):
    return ''.join(random.sample(string.ascii_letters + string.digits, 8))


# db.create_all()
if __name__ == '__main__':
    # db.create_all()
    # 创建session对象:
    session = db.session()
    # 创建新User对象:
    print(time.time())
    for key in range(2500):
        new_user = User(name=f'Bob{get_random_text(3)}',
                        age=17, sign='fuck you', email=f'{get_random_text(10)}@qq.com')
        # 添加到session:
        session.add(new_user)

    print(time.time())
    # 提交即保存到数据库:
    session.commit()
    print(time.time())

    # 关闭session:
    session.close()
