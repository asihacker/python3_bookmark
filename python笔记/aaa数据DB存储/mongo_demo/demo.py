#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 22:06
# @Author  : AsiHacker
# @File    : json模块.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import datetime
import time

import pandas as pd
from pymongo import MongoClient

# https://blog.csdn.net/qq_33961117/article/details/90668555
# https://zhuanlan.zhihu.com/p/79032970
client = MongoClient(host='mongodb://47.115.20.50:27017')  # 连接服务器
client.admin.authenticate('root', 'Nantian@NS2020')  # 认证权限
db = client["okooo"]  # 选择数据库
collection = db['okooo']  # 选择集合
# res = collection.find({'matchid': 213039})  # 查询集合
# print(next(res))
# res = collection.count_documents({'matchid': 213039})  # 查询数量
# print(res)
while 1:
    time.sleep(3)
    res = collection.estimated_document_count()  # 查询数量
    print(res)
# res = collection.find({"matchid": {"$in": [213039, 208286]}})#$nin是不在里面的
# res = collection.count_documents({"matchid": {"$in": [213039, 208286]}})  # in查询
# print(res)
# res = collection.find({"matchid": {"$in": [213039, 208286, 93939393]}}, {'matchid': 1})  # in查询返回指定字段
# print(res)
# res = collection.count_documents({'time': {'$lte': datetime.datetime(year=2012, month=11, day=1),
#                                            '$gte': datetime.datetime(year=2012, month=10, day=1)}})
# print(res)

# res = collection.find({'time': {'$gte': datetime.datetime(year=2012, month=11, day=1),
#                                 '$lte': datetime.datetime(year=2012, month=12, day=1)}},
#                       {'matchid': 1,
#                        'time': 1,
#                        'match': 1,
#                        'home': 1,
#                        'customer': 1,
#                        'score_h': 1,
#                        'score_c': 1,
#                        'sfzs_h_win_1': 1,
#                        'sfzs_h_tie_1': 1,
#                        'sfzs_h_lose_1': 1,
#                        'sfzs_h_get_1': 1,
#                        'sfzs_h_pop_1': 1,
#                        'sfzs_h_win_2': 1,
#                        'sfzs_h_tie_2': 1,
#                        'sfzs_h_lose_2': 1,
#                        'sfzs_h_get_2': 1,
#                        'sfzs_h_pop_2': 1,
#                        'sfzs_c_win_1': 1,
#                        'sfzs_c_tie_1': 1,
#                        'sfzs_c_lose_1': 1,
#                        'sfzs_c_get_1': 1,
#                        'sfzs_c_pop_1': 1,
#                        'sfzs_c_win_2': 1,
#                        'sfzs_c_tie_2': 1,
#                        'sfzs_c_lose_2': 1,
#                        'sfzs_c_get_2': 1,
#                        'sfzs_c_pop_2': 1,
#                        'odds_avg': 1,
#                        'ah_avg': 1,
#                        'overunder_avg': 1,
#                        'result': 1,
#                        }
#                       ).limit(5000)  # in查询返回指定字段
# matchid = []
# time = []
# match = []
# home = []
# customer = []
# score_h = []
# score_c = []
# sfzs_h_win_1 = []
# sfzs_h_tie_1 = []
# sfzs_h_lose_1 = []
# sfzs_h_get_1 = []
# sfzs_h_pop_1 = []
# sfzs_h_win_2 = []
# sfzs_h_tie_2 = []
# sfzs_h_lose_2 = []
# sfzs_h_get_2 = []
# sfzs_h_pop_2 = []
# sfzs_c_win_1 = []
# sfzs_c_tie_1 = []
# sfzs_c_lose_1 = []
# sfzs_c_get_1 = []
# sfzs_c_pop_1 = []
# sfzs_c_win_2 = []
# sfzs_c_tie_2 = []
# sfzs_c_lose_2 = []
# sfzs_c_get_2 = []
# sfzs_c_pop_2 = []
# odds_1 = []
# odds_2 = []
# odds_3 = []
# odds_4 = []
# odds_5 = []
# odds_6 = []
# odds_7 = []
# odds_8 = []
# odds_9 = []
# odds_10 = []
# odds_11 = []
# odds_12 = []
# odds_13 = []
# odds_14 = []
# odds_15 = []
# odds_16 = []
# odds_17 = []
# odds_18 = []
# odds_19 = []
# odds_20 = []
# odds_21 = []
# odds_22 = []
# odds_23 = []
# odds_24 = []
# odds_25 = []
# odds_26 = []
# odds_27 = []
# odds_28 = []
# odds_29 = []
# odds_30 = []
# odds_31 = []
# odds_32 = []
# odds_33 = []
# odds_34 = []
# odds_35 = []
# odds_36 = []
# odds_37 = []
# odds_38 = []
# odds_39 = []
# odds_40 = []
# odds_41 = []
# odds_42 = []
# odds_43 = []
# odds_44 = []
# odds_45 = []
# odds_46 = []
# odds_47 = []
# odds_48 = []
# odds_49 = []
# ah_1 = []
# ah_2 = []
# ah_3 = []
# ah_4 = []
# ah_5 = []
# ah_6 = []
# ah_7 = []
# ah_8 = []
# ah_9 = []
# ah_10 = []
# ah_11 = []
# ah_12 = []
# ah_13 = []
# ah_14 = []
# ah_15 = []
# ah_16 = []
# ah_17 = []
# ah_18 = []
# ah_19 = []
# ah_20 = []
# ah_21 = []
# ah_22 = []
# ah_23 = []
# ah_24 = []
# ah_25 = []
# ah_26 = []
# ah_27 = []
# ah_28 = []
# ah_29 = []
# ah_30 = []
# ah_31 = []
# ah_32 = []
# ah_33 = []
# ah_34 = []
# overunder_1 = []
# overunder_2 = []
# overunder_3 = []
# overunder_4 = []
# overunder_5 = []
# overunder_6 = []
# overunder_7 = []
# overunder_8 = []
# overunder_9 = []
# overunder_10 = []
# overunder_11 = []
# overunder_12 = []
# overunder_13 = []
# overunder_14 = []
# overunder_15 = []
# overunder_16 = []
# overunder_17 = []
# overunder_18 = []
# overunder_19 = []
# overunder_20 = []
# overunder_21 = []
# overunder_22 = []
# overunder_23 = []
# overunder_24 = []
# overunder_25 = []
# overunder_26 = []
# overunder_27 = []
# overunder_28 = []
# overunder_29 = []
# overunder_30 = []
# overunder_31 = []
# overunder_32 = []
# overunder_33 = []
# overunder_34 = []
# overunder_35 = []
# overunder_36 = []
# overunder_37 = []
# overunder_38 = []
# overunder_39 = []
# overunder_40 = []
# result = []
# for one in res:
#     print(one['matchid'])
#     matchid.append(one['matchid'])
#     time.append(one['time'])
#     match.append(one['match'])
#     home.append(one['home'])
#     customer.append(one['customer'])
#     score_h.append(one['score_h'])
#     score_c.append(one['score_c'])
#     sfzs_h_win_1.append(one['sfzs_h_win_1'])
#     sfzs_h_tie_1.append(one['sfzs_h_tie_1'])
#     sfzs_h_lose_1.append(one['sfzs_h_lose_1'])
#     sfzs_h_get_1.append(one['sfzs_h_get_1'])
#     sfzs_h_pop_1.append(one['sfzs_h_pop_1'])
#     sfzs_h_win_2.append(one['sfzs_h_win_2'])
#     sfzs_h_tie_2.append(one['sfzs_h_tie_2'])
#     sfzs_h_lose_2.append(one['sfzs_h_lose_2'])
#     sfzs_h_get_2.append(one['sfzs_h_get_2'])
#     sfzs_h_pop_2.append(one['sfzs_h_pop_2'])
#     sfzs_c_win_1.append(one['sfzs_c_win_1'])
#     sfzs_c_tie_1.append(one['sfzs_c_tie_1'])
#     sfzs_c_lose_1.append(one['sfzs_c_lose_1'])
#     sfzs_c_get_1.append(one['sfzs_c_get_1'])
#     sfzs_c_pop_1.append(one['sfzs_c_pop_1'])
#     sfzs_c_win_2.append(one['sfzs_c_win_2'])
#     sfzs_c_tie_2.append(one['sfzs_c_tie_2'])
#     sfzs_c_lose_2.append(one['sfzs_c_lose_2'])
#     sfzs_c_get_2.append(one['sfzs_c_get_2'])
#     sfzs_c_pop_2.append(one['sfzs_c_pop_2'])
#     odds_1.append(one['odds_avg']['count'])
#     odds_2.append(float(one['odds_avg']['max']['Start']['home']))
#     odds_3.append(float(one['odds_avg']['max']['Start']['draw']))
#     odds_4.append(float(one['odds_avg']['max']['Start']['away']))
#     odds_5.append(float(one['odds_avg']['max']['End']['home']))
#     odds_6.append(float(one['odds_avg']['max']['End']['draw']))
#     odds_7.append(float(one['odds_avg']['max']['End']['away']))
#     odds_8.append(float(one['odds_avg']['max']['Radio']['home']))
#     odds_9.append(float(one['odds_avg']['max']['Radio']['draw']))
#     odds_10.append(float(one['odds_avg']['max']['Radio']['away']))
#     odds_11.append(float(one['odds_avg']['max']['Kelly']['home']))
#     odds_12.append(float(one['odds_avg']['max']['Kelly']['draw']))
#     odds_13.append(float(one['odds_avg']['max']['Kelly']['away']))
#     odds_14.append(float(one['odds_avg']['max']['Payoff']))
#     odds_15.append(float(one['odds_avg']['min']['Start']['home']))
#     odds_16.append(float(one['odds_avg']['min']['Start']['draw']))
#     odds_17.append(float(one['odds_avg']['min']['Start']['away']))
#     odds_18.append(float(one['odds_avg']['min']['End']['home']))
#     odds_19.append(float(one['odds_avg']['min']['End']['draw']))
#     odds_20.append(float(one['odds_avg']['min']['End']['away']))
#     odds_21.append(float(one['odds_avg']['min']['Radio']['home']))
#     odds_22.append(float(one['odds_avg']['min']['Radio']['draw']))
#     odds_23.append(float(one['odds_avg']['min']['Radio']['away']))
#     odds_24.append(float(one['odds_avg']['min']['Kelly']['home']))
#     odds_25.append(float(one['odds_avg']['min']['Kelly']['draw']))
#     odds_26.append(float(one['odds_avg']['min']['Kelly']['away']))
#     odds_27.append(float(one['odds_avg']['min']['Payoff']))
#     odds_28.append(float(one['odds_avg']['avg']['Start']['home']))
#     odds_29.append(float(one['odds_avg']['avg']['Start']['draw']))
#     odds_30.append(float(one['odds_avg']['avg']['Start']['away']))
#     odds_31.append(float(one['odds_avg']['avg']['End']['home']))
#     odds_32.append(float(one['odds_avg']['avg']['End']['draw']))
#     odds_33.append(float(one['odds_avg']['avg']['End']['away']))
#     odds_34.append(float(one['odds_avg']['avg']['Radio']['home']))
#     odds_35.append(float(one['odds_avg']['avg']['Radio']['draw']))
#     odds_36.append(float(one['odds_avg']['avg']['Radio']['away']))
#     odds_37.append(float(one['odds_avg']['avg']['Kelly']['home']))
#     odds_38.append(float(one['odds_avg']['avg']['Kelly']['draw']))
#     odds_39.append(float(one['odds_avg']['avg']['Kelly']['away']))
#     odds_40.append(float(one['odds_avg']['avg']['Payoff']))
#     odds_41.append(float(one['odds_avg']['variance']['KD']['home']))
#     odds_42.append(float(one['odds_avg']['variance']['KD']['draw']))
#     odds_43.append(float(one['odds_avg']['variance']['KD']['away']))
#     odds_44.append(float(one['odds_avg']['variance']['KV']['home']))
#     odds_45.append(float(one['odds_avg']['variance']['KV']['draw']))
#     odds_46.append(float(one['odds_avg']['variance']['KV']['away']))
#     odds_47.append(float(one['odds_avg']['variance']['OE']['home']))
#     odds_48.append(float(one['odds_avg']['variance']['OE']['draw']))
#     odds_49.append(float(one['odds_avg']['variance']['OE']['away']))
#     ah_1.append(one['ah_avg']['count'])
#     ah_2.append(float(one['ah_avg']['max']['Start']['home']))
#     ah_3.append(float(one['ah_avg']['max']['Start']['away']))
#     ah_4.append(float(one['ah_avg']['max']['Start']['boundary']))
#     ah_5.append(float(one['ah_avg']['max']['End']['home']))
#     ah_6.append(float(one['ah_avg']['max']['End']['away']))
#     ah_7.append(float(one['ah_avg']['max']['End']['boundary']))
#     ah_8.append(float(one['ah_avg']['max']['Radio']['home']))
#     ah_9.append(float(one['ah_avg']['max']['Radio']['away']))
#     ah_10.append(float(one['ah_avg']['max']['Payoff']))
#     ah_11.append(float(one['ah_avg']['max']['Boundary']))
#     ah_12.append(float(one['ah_avg']['max']['StartBoundary']))
#     ah_13.append(float(one['ah_avg']['min']['Start']['home']))
#     ah_14.append(float(one['ah_avg']['min']['Start']['away']))
#     ah_15.append(float(one['ah_avg']['min']['Start']['boundary']))
#     ah_16.append(float(one['ah_avg']['min']['End']['home']))
#     ah_17.append(float(one['ah_avg']['min']['End']['away']))
#     ah_18.append(float(one['ah_avg']['min']['End']['boundary']))
#     ah_19.append(float(one['ah_avg']['min']['Radio']['home']))
#     ah_20.append(float(one['ah_avg']['min']['Radio']['away']))
#     ah_21.append(float(one['ah_avg']['min']['Payoff']))
#     ah_22.append(float(one['ah_avg']['min']['Boundary']))
#     ah_23.append(float(one['ah_avg']['min']['StartBoundary']))
#     ah_24.append(float(one['ah_avg']['avg']['Start']['home']))
#     ah_25.append(float(one['ah_avg']['avg']['Start']['away']))
#     ah_26.append(float(one['ah_avg']['avg']['Start']['boundary']))
#     ah_27.append(float(one['ah_avg']['avg']['End']['home']))
#     ah_28.append(float(one['ah_avg']['avg']['End']['away']))
#     ah_29.append(float(one['ah_avg']['avg']['End']['boundary']))
#     ah_30.append(float(one['ah_avg']['avg']['Radio']['home']))
#     ah_31.append(float(one['ah_avg']['avg']['Radio']['away']))
#     ah_32.append(float(one['ah_avg']['avg']['Payoff']))
#     ah_33.append(float(one['ah_avg']['avg']['Boundary']))
#     ah_34.append(float(one['ah_avg']['avg']['StartBoundary']))
#     overunder_1.append(one['overunder_avg']['count'])
#     overunder_2.append(float(one['overunder_avg']['max']['Start']['over']))
#     overunder_3.append(float(one['overunder_avg']['max']['Start']['under']))
#     overunder_4.append(float(one['overunder_avg']['max']['Start']['boundary']))
#     overunder_5.append(float(one['overunder_avg']['max']['End']['over']))
#     overunder_6.append(float(one['overunder_avg']['max']['End']['under']))
#     overunder_7.append(float(one['overunder_avg']['max']['End']['boundary']))
#     overunder_8.append(float(one['overunder_avg']['max']['Radio']['over']))
#     overunder_9.append(float(one['overunder_avg']['max']['Radio']['under']))
#     overunder_10.append(float(one['overunder_avg']['max']['Payoff']))
#     overunder_11.append(float(one['overunder_avg']['max']['Boundary']))
#     overunder_12.append(float(one['overunder_avg']['max']['StartBoundary']))
#     try:
#         overunder_13.append(float(one['overunder_avg']['max']['Kelly']['over']))
#         overunder_14.append(float(one['overunder_avg']['max']['Kelly']['under']))
#     except:
#         overunder_13.append(None)
#         overunder_14.append(None)
#     overunder_15.append(float(one['overunder_avg']['min']['Start']['over']))
#     overunder_16.append(float(one['overunder_avg']['min']['Start']['under']))
#     overunder_17.append(float(one['overunder_avg']['min']['Start']['boundary']))
#     overunder_18.append(float(one['overunder_avg']['min']['End']['over']))
#     overunder_19.append(float(one['overunder_avg']['min']['End']['under']))
#     overunder_20.append(float(one['overunder_avg']['min']['End']['boundary']))
#     overunder_21.append(float(one['overunder_avg']['min']['Radio']['over']))
#     overunder_22.append(float(one['overunder_avg']['min']['Radio']['under']))
#     overunder_23.append(float(one['overunder_avg']['min']['Payoff']))
#     overunder_24.append(float(one['overunder_avg']['min']['Boundary']))
#     overunder_25.append(float(one['overunder_avg']['min']['StartBoundary']))
#     try:
#         overunder_26.append(float(one['overunder_avg']['min']['Kelly']['over']))
#         overunder_27.append(float(one['overunder_avg']['min']['Kelly']['under']))
#     except:
#         overunder_26.append(None)
#         overunder_27.append(None)
#     overunder_28.append(float(one['overunder_avg']['avg']['Start']['over']))
#     overunder_29.append(float(one['overunder_avg']['avg']['Start']['under']))
#     overunder_30.append(float(one['overunder_avg']['avg']['Start']['boundary']))
#     overunder_31.append(float(one['overunder_avg']['avg']['End']['over']))
#     overunder_32.append(float(one['overunder_avg']['avg']['End']['under']))
#     overunder_33.append(float(one['overunder_avg']['avg']['End']['boundary']))
#     overunder_34.append(float(one['overunder_avg']['avg']['Radio']['over']))
#     overunder_35.append(float(one['overunder_avg']['avg']['Radio']['under']))
#     overunder_36.append(float(one['overunder_avg']['avg']['Payoff']))
#     overunder_37.append(float(one['overunder_avg']['avg']['Boundary']))
#     overunder_38.append(float(one['overunder_avg']['avg']['StartBoundary']))
#     try:
#         overunder_39.append(float(one['overunder_avg']['avg']['Kelly']['over']))
#         overunder_40.append(float(one['overunder_avg']['avg']['Kelly']['under']))
#     except:
#         overunder_39.append(None)
#         overunder_40.append(None)
#     result.append(one['result'])
#
# # 任意的多组列表
#
# # 字典中的key值即为csv中列名
# dataframe = pd.DataFrame({
#     'matchid': matchid,
#     'time': time,
#     'match': match,
#     'home': home,
#     'customer': customer,
#     'score_h': score_h,
#     'score_c': score_c,
#     'result': result,
#     'sfzs_h_win_1': sfzs_h_win_1,
#     'sfzs_h_tie_1': sfzs_h_tie_1,
#     'sfzs_h_lose_1': sfzs_h_lose_1,
#     'sfzs_h_get_1': sfzs_h_get_1,
#     'sfzs_h_pop_1': sfzs_h_pop_1,
#     'sfzs_h_win_2': sfzs_h_win_2,
#     'sfzs_h_tie_2': sfzs_h_tie_2,
#     'sfzs_h_lose_2': sfzs_h_lose_2,
#     'sfzs_h_get_2': sfzs_h_get_2,
#     'sfzs_h_pop_2': sfzs_h_pop_2,
#     'sfzs_c_win_1': sfzs_c_win_1,
#     'sfzs_c_tie_1': sfzs_c_tie_1,
#     'sfzs_c_lose_1': sfzs_c_lose_1,
#     'sfzs_c_get_1': sfzs_c_get_1,
#     'sfzs_c_pop_1': sfzs_c_pop_1,
#     'sfzs_c_win_2': sfzs_c_win_2,
#     'sfzs_c_tie_2': sfzs_c_tie_2,
#     'sfzs_c_lose_2': sfzs_c_lose_2,
#     'sfzs_c_get_2': sfzs_c_get_2,
#     'sfzs_c_pop_2': sfzs_c_pop_2,
#     'odds_1': odds_1,
#     'odds_2': odds_2,
#     'odds_3': odds_3,
#     'odds_4': odds_4,
#     'odds_5': odds_5,
#     'odds_6': odds_6,
#     'odds_7': odds_7,
#     'odds_8': odds_8,
#     'odds_9': odds_9,
#     'odds_10': odds_10,
#     'odds_11': odds_11,
#     'odds_12': odds_12,
#     'odds_13': odds_13,
#     'odds_14': odds_14,
#     'odds_15': odds_15,
#     'odds_16': odds_16,
#     'odds_17': odds_17,
#     'odds_18': odds_18,
#     'odds_19': odds_19,
#     'odds_20': odds_20,
#     'odds_21': odds_21,
#     'odds_22': odds_22,
#     'odds_23': odds_23,
#     'odds_24': odds_24,
#     'odds_25': odds_25,
#     'odds_26': odds_26,
#     'odds_27': odds_27,
#     'odds_28': odds_28,
#     'odds_29': odds_29,
#     'odds_30': odds_30,
#     'odds_31': odds_31,
#     'odds_32': odds_32,
#     'odds_33': odds_33,
#     'odds_34': odds_34,
#     'odds_35': odds_35,
#     'odds_36': odds_36,
#     'odds_37': odds_37,
#     'odds_38': odds_38,
#     'odds_39': odds_39,
#     'odds_40': odds_40,
#     'odds_41': odds_41,
#     'odds_42': odds_42,
#     'odds_43': odds_43,
#     'odds_44': odds_44,
#     'odds_45': odds_45,
#     'odds_46': odds_46,
#     'odds_47': odds_47,
#     'odds_48': odds_48,
#     'odds_49': odds_49,
#     'ah_1': ah_1,
#     'ah_2': ah_2,
#     'ah_3': ah_3,
#     'ah_4': ah_4,
#     'ah_5': ah_5,
#     'ah_6': ah_6,
#     'ah_7': ah_7,
#     'ah_8': ah_8,
#     'ah_9': ah_9,
#     'ah_10': ah_10,
#     'ah_11': ah_11,
#     'ah_12': ah_12,
#     'ah_13': ah_13,
#     'ah_14': ah_14,
#     'ah_15': ah_15,
#     'ah_16': ah_16,
#     'ah_17': ah_17,
#     'ah_18': ah_18,
#     'ah_19': ah_19,
#     'ah_20': ah_20,
#     'ah_21': ah_21,
#     'ah_22': ah_22,
#     'ah_23': ah_23,
#     'ah_24': ah_24,
#     'ah_25': ah_25,
#     'ah_26': ah_26,
#     'ah_27': ah_27,
#     'ah_28': ah_28,
#     'ah_29': ah_29,
#     'ah_30': ah_30,
#     'ah_31': ah_31,
#     'ah_32': ah_32,
#     'ah_33': ah_33,
#     'ah_34': ah_34,
#     'overunder_1': overunder_1,
#     'overunder_2': overunder_2,
#     'overunder_3': overunder_3,
#     'overunder_4': overunder_4,
#     'overunder_5': overunder_5,
#     'overunder_6': overunder_6,
#     'overunder_7': overunder_7,
#     'overunder_8': overunder_8,
#     'overunder_9': overunder_9,
#     'overunder_10': overunder_10,
#     'overunder_11': overunder_11,
#     'overunder_12': overunder_12,
#     'overunder_13': overunder_13,
#     'overunder_14': overunder_14,
#     'overunder_15': overunder_15,
#     'overunder_16': overunder_16,
#     'overunder_17': overunder_17,
#     'overunder_18': overunder_18,
#     'overunder_19': overunder_19,
#     'overunder_20': overunder_20,
#     'overunder_21': overunder_21,
#     'overunder_22': overunder_22,
#     'overunder_23': overunder_23,
#     'overunder_24': overunder_24,
#     'overunder_25': overunder_25,
#     'overunder_26': overunder_26,
#     'overunder_27': overunder_27,
#     'overunder_28': overunder_28,
#     'overunder_29': overunder_29,
#     'overunder_30': overunder_30,
#     'overunder_31': overunder_31,
#     'overunder_32': overunder_32,
#     'overunder_33': overunder_33,
#     'overunder_34': overunder_34,
#     'overunder_35': overunder_35,
#     'overunder_36': overunder_36,
#     'overunder_37': overunder_37,
#     'overunder_38': overunder_38,
#     'overunder_39': overunder_39,
#     'overunder_40': overunder_40,
# })
# # 将DataFrame存储为csv,index表示是否显示行名，default=True
# dataframe.to_csv("debug.csv", index=False)
