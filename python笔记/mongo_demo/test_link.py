# MongoClient的第一个参数host还可以直接传MongoDB的连接字符串，以mongodb开头
from pymongo import MongoClient

client = MongoClient(host='mongodb://ntkj:nantian888@8.129.216.60:27017')  # 连接服务器
db = client["asihacker"]  # 选择数据库
collection = db['test222']  # 选择集合
###### 插入一条数据 ######
student = {
    'name': 'Jordan',
    'age': 18,
    'gender': 'man'
}

result = db.collection.insert_one(student)
# insert()返回执行后文档的主键'_id'的值
print(result.inserted_id)  # 5932a68615c2606814c91f3d

######  插入多条数据  ######
student1 = {
    'name': 'Jordan',
    'age': 10,
    'gender': 'man'
}

student2 = {
    'name': 'Mike',
    'age': 11,
    'gender': 'man'
}

result = collection.insert_many([student1, student2])
# insert()返回执行后文档的主键'_id'的集合
print(result.inserted_ids)  # [ObjectId('5932a80115c2606a59e8a048'), ObjectId('5932a80115c2606a59e8a049')]
# 增删查改教程地址 https://www.cnblogs.com/cangqinglang/p/12030495.html
