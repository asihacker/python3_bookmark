#!/usr/bin/python
# coding=utf-8


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
a = [3, 4, 5, 6, 2, 2, 3, 1, 2, 4, 6, 7, 86, 554, 45, 5]
a.sort(reverse=True)
print(a)

print(students.sort(key=lambda items: items['math']))
print(students)
