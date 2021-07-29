from sqlalchemy import create_engine
from sqlalchemy.engine import reflection

test = """
# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = (
        db.Index('uk_user_id_role_id', 'user_id', 'role_id'),
        db.Index('uk_user_id_role_id', 'user_id', 'role_id'),
        db.Index('uk_user_id_role_id', 'user_id', 'role_id'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(32, 'utf8mb4_general_ci'), nullable=False, unique=True)
    password_hash = db.Column(db.String(40, 'utf8mb4_general_ci'), nullable=False)
    gmt_create = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='创建时间')
    gmt_modified = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue(), info='更新时间')
"""
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ds_data_takumi_test?charset=utf8mb4')
insp = reflection.Inspector.from_engine(engine)
columns = insp.get_columns('nt_whatsapp_send_task_log')  # 这里是写的表名
for column in columns:
    print(column)
#     if column['default'] is not None:
#         test = test.replace('db.FetchedValue()', f'db.text("{column["default"]}")', 1)
#     if column['comment'] is not None:
#         test = test.replace(', info=', f', comment={column["comment"]}, doc=',1)
# test = test.replace('from flask_sqlalchemy import SQLAlchemy', 'from app.extensions import db,ma')
# test = test.replace('db = SQLAlchemy()', '').replace('\n' * 3, '')
# table_comment = {'comment': insp.get_table_comment("user")['text']}
# if '__table_args__' in test:
#     test = test.replace(',\n    )', f',\n        {table_comment},\n    )')
#     pass
# else:
#     test = test.replace('\n\n', f'\n    __table_args__ = {table_comment}\n')
# class_name = test[test.find('class ') + 6:test.find('(db.Model):')]
# schema = '\n'.join([f'class {class_name}Schema(ma.SQLAlchemyAutoSchema)', '    class Meta:', f'        model = {class_name}'])
#
# print('\n'.join([test, schema]))
