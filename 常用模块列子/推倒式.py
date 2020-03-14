#!/usr/bin/python
# coding=utf-8
# TODO:推导式
a_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
a_list = [key for key in a_dict]
print(a_list)
a_list = [a_dict[key] for key in a_dict]
print(a_list)
a_list = [k for k, v in a_dict.items()]
print(a_list)
b_dict = {k: v for k, v in a_dict.items() if v > 3}
print(b_dict)
# TODO:strip,lstrip,rstrip
a_str = '<abCDefgaaa>'
b_str = 'asi'
print(a_str.strip('>'))  # 去除头部和尾部包含'<'
print(a_str.strip('<'))
print(a_str.strip('<').strip('>'))
print(a_str.lstrip('<'))  # 去除头部包含'<'
print(a_str.rstrip('>'))  # 去除头部包含'<'
# strip,lstrip,rstrip不填参数，默认去掉，\n,\r,\t
print(a_str.strip('<').capitalize())  # capitalize把字符串第一个字母大写（第一个不是字母则失效）
print(a_str.casefold())  # Python casefold() 方法是Python3.3版本之后引入的，其效果和 lower() 方法非常相似，都可以转换字符串中所有大写字符为小写。
# 两者的区别是：lower() 方法只对ASCII编码，也就是‘A-Z’有效，对于其他语言（非汉语或英文）中把大写转换为小写的情况只能用 casefold() 方法。
print(a_str.encode('UTF-8'))  # 编码
print(a_str.index('e'))  # 找不到会抛出异常
print(a_str.find('e'))  # 找不到返回-1
print(a_str.center(20, "*"))
print(b_str.center(20, "*"))
# ********asi*********
print(a_str.count('f'))  # 计算字符串出现的次数
print(a_str.isalnum())  # isal类型，都是判断字符串是否存在，返回正假
print(b_str.isalpha())
print(a_str.endswith('>'))  # 用于判断字符串是否以指定后缀结尾
print(a_str.startswith('<'))  # 用于判断字符串是否以指定后缀结尾
print(a_str.replace('a', 'A', 2))  # 替换字符串
print(a_str.split('a'))  # 分割字符串
print(a_str.ljust(20, '*'))
print(a_str.rjust(20, '*'))
print(a_str.upper())
print(a_str.lower())
# <abCDefgaaa>********
# ********<abCDefgaaa>
# TODO:all(),any()
print(all([1, 1, 1, 1]))
print(all([1, 1, 1, 0]))
print(any([1, 1, 1, 0]))
# TODO:lambda匿名函数


# TODO:列表排序与字典排序
students = [{"name": "zhangsan1", "math": "89", "english": "87"},
            {"name": "zhangsan2", "math": "65", "english": "87"},
            {"name": "zhangsan3", "math": "99", "english": "87"},
            {"name": "zhangsan4", "math": "55", "english": "87"},
            ]
aaa = lambda item: item.get('math')
print(aaa(students[0]))
students.sort(key=lambda item: item.get('math'), reverse=True)
print(students)
students = [{"name": "zhangsan1", "math": "89", "english": "87"},
            {"name": "zhangsan2", "math": "65", "english": "87"},
            {"name": "zhangsan3", "math": "99", "english": "87"},
            {"name": "zhangsan4", "math": "55", "english": "87"},
            ]
result = sorted(students, key=lambda student: student['math'], reverse=True)
print(result)
print(students)

zhangsan = {"math": "89", "english": "87", "chinese": "99"}
result = sorted(zhangsan.items(), key=lambda item: item[1], reverse=True)
print(result)
print(zhangsan)
print(zhangsan.items())
