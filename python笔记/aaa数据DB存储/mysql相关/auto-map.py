# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 13:19
# @Author  : AsiHacker
# @File    : auto-map
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

Base = automap_base()

# 我们假设数据库中存在两张表 `user` 和 `address`。
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/ds_data_takumi_test?charset=utf8mb4")
# 将数据库中的表全部映射到 Base.classes 中
Base.prepare(engine, reflect=True)
# 映射类的默认名为数据表的名称
# 可以通过数据表名访问
User = Base.classes.user
