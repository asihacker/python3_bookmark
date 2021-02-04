#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 18:31
# @Author  : AsiHacker
# @File    : redis常用方法.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import redis

# https://www.cnblogs.com/john-xiong/p/12089103.html
redisPool = redis.ConnectionPool(host='192.168.100.50', port=6379, db=8)
redis = redis.Redis(connection_pool=redisPool)

redis.set('key', 'values')
redis.get('com')
redis.append('keys', 'values')
redis.delete('keys')

print(redis.getset('name', 'Mike'))  # 赋值name为Mike并返回上一次的value
print(redis.mget(['name', 'age']))  # 输出name键和age键的value
print(redis.setnx('newname', 'james'))  # 如果键值不存在，则赋值
print(redis.mset({'name1': 'smith', 'name2': 'curry'}))  # 批量赋值
print(redis.msetnx({'name3': 'ltf', 'name4': 'lsq'}))  # 不存在才批量赋值
print(redis.incr('age', 1))  # age对应的value 加1
print(redis.decr('age', 5))  # age对应的value 减5
print(redis.append('name4', 'is a sb'))  # 在name4的value后追加 is a sb 返回字符串长度
print(redis.substr('name', 1, 4))  # 截取键 name

print(redis.sadd('tags', 'Book', 'Tea', 'Coffee'))  # 返回集合长度 3
print(redis.srem('tags', 'Book'))  # 返回删除的数据个数
print(redis.spop('tags'))  # 随机删除并返回该元素
print(redis.smove('tags', 'tags1', 'Coffee'))
print(redis.scard('tags'))  # 获取tags集合的元素个数
print(redis.sismember('tags', 'Book'))  # 判断Book是否在tags的集合中
print(redis.sinter('tags', 'tags1'))  # 返回集合tags和集合tags1的交集
print(redis.sunion('tags', 'tags1'))  # 返回集合tags和集合tags1的并集
print(redis.sdiff('tags', 'tags1'))  # 返回集合tags和集合tags1的差集
print(redis.smembers('tags'))  # 返回集合tags的所有元素

print(redis.hset('price', 'cake', 5))  # 向键名为price的散列表添加映射关系，返回1 即添加的映射个数
print(redis.hsetnx('price', 'book', 6))  # 向键名为price的散列表添加映射关系，返回1 即添加的映射个数
print(redis.hget('price', 'cake'))  # 获取键名为cake的值 返回5
print(redis.hmset('price', {'banana': 2, 'apple': 3, 'pear': 6, 'orange': 7}))  # 批量添加映射
print(redis.hmget('price', ['apple', 'orange']))  # 查询apple和orange的值 输出 b'3',b'7'
print(redis.hincrby('price', 'apple', 3))  # apple映射加3 为6
print(redis.hexists('price', 'banana'))  # 在price中banana是否存在  返回True
print(redis.hdel('price', 'banana'))  # 从price中删除banana 返回1
print(redis.hlen('price'))  # 输出price的长度
print(redis.hkeys('price'))  # 输出所有的映射键名
print(redis.hvals('price'))  # 输出所有的映射键值
print(redis.hgetall('price'))  # 输出所有的映射键对

print(redis.rpush('list', 1, 2, 3))  # 向键名为list的列表尾部添加1,2,3 返回长度
print(redis.lpush('list', 0))  # 向键名为list的列表头部添加0 返回长度
print(redis.llen('list'))  # 返回列表的长度
print(redis.lrange('list', 1, 3))  # 返回起始索引为1 终止索引为3的索引范围对应的列表
print(redis.lindex('list', 1))  # 返回索引为1的元素-value
print(redis.lset('list', 1, 5))  # 将list的列表索引为1的重新赋值为5
print(redis.lpop('list'))  # 删除list第一个元素
print(redis.rpop('list'))  # 删除list最后一个元素
print(redis.blpop('list'))  # 删除list第一个元素
print(redis.brpop('list'))  # 删除最后一个元素
print(redis.rpoplpush('list', 'list1'))  # 删除list的尾元素并将其添加到list1的头部
print(redis.keys('ssr*'))  # 正则获取key
