# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 12:25
# @Author  : AsiHacker
# @File    : 自动分表
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
AutoBase = automap_base()

# reflect the tables
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ds_data_takumi_test?charset=utf8mb4')
BaseSQL = declarative_base()
BaseSQL.metadata.reflect(engine)
table_obj = BaseSQL.metadata.tables['nt_whatsapp_send_task_log']
for index in table_obj.indexes:
    print(index)