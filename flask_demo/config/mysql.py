#!/usr/bin/python
# # coding=utf-8
DIALECT = 'mysql'  # 数据库类型
DRIVER = 'pymysql'  # 驱动
USERNAME = 'root'  # 用户名
PASSWORD = '123456'  # 密码
HOST = '127.0.0.1'  # 数据库ip
PORT = '3306'  # 端口
DATABASE = 'asihacker'  # 数据库名称
SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 自动提交省去了每次 commit
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_ECHO = True  # 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
SQLALCHEMY_POOL_SIZE = 50  # 连接池的大小，默认为5个，设置为0时表示连接无限制
SQLALCHEMY_POOL_RECYCLE = 60 * 30  # 设置时间以限制数据库多久没连接自动断开
SQLALCHEMY_POOL_TIMEOUT = 15  # 指定数据库连接池的超时时间。默认是 10。
SQLALCHEMY_MAX_OVERFLOW = 30  # 控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。
