#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 20:14
# @Author  : AsiHacker
# @Site    : 
# @File    : mingyanSpider.py
# @Software: PyCharm
import re


def test():
    """"""
    # 1. compile(正则表达式)   -> 将正则表达式转换成正则对象
    """
    编译后可以直接通过对象调用相关的对象方法 
    """
    re_object = re.compile(r'\d{3}')
    re_object.fullmatch('432')

    # 2. fullmatch(正则表达式, 字符串)  -> 让字符串和正则表达式完全匹配，匹配成功返回匹配对象，匹配失败返回None
    """
    应用：检测字符串内容是否符合要求,例如：检测账号、密码、判断手机号、身份证号等是否合法
    """
    result = re.fullmatch(r'(\d{3})=([a-z]+)', '342=sjaks')
    print(result)

    # 匹配对象
    # 1).span() - 匹配到的字符串在原字符串中的下标范围(结果是元素)
    print('====span====')
    print(result.span())  # 获取整个正则表达式匹配到的内容的范围
    # start, end = result.span()
    # print(start, end)

    print(result.span(1))  # 获取正则表达式中第一个分组匹配到的内容的范围
    print(result.span(2))  # 获取正则表达式中第二个分组匹配到的内容的范围

    # 2). start()和end() - 匹配到的字符串在原字符串中的开始下标和结束下标
    print('====start名，end====')
    print(result.start(), result.end())
    print(result.start(1), result.start(2))

    # 3). group()  -  获取匹配到的字符串(结果是字符串)
    print(result.group())  # 获取整个正则匹配到的字符串
    print(result.group(1))  # 获取第一个分组匹配到的字符串
    print(result.group(2))  # 获取第二个分组匹配到的字符串
    print(result.groups())  # 同时获取所有分组匹配到的字符串(结果是元祖)

    # 4). string - 获取原字符串
    print(result.string)

    # 3.match(正则表达式,字符串) -> 让字符串的开头和正则表达式进行匹配，匹配成功结果是匹配对象，否则是None
    print(re.match(r'\D\d', 's3skjkjks'))

    # 4.search(正则表达式,字符串) -> 在字符串中去匹配出第一个符合正则表达式的子串, 匹配成功结果是匹配对象,否则是None
    print(re.search(r'[\u4e00-\u9fa5]{3}', 'hsj后视ss023你好吗,skss上的30s'))

    # 5.split(正则表达式,字符串) -> 将字符串按照满足正则要求的子串进行切割(返回值是列表)
    print(re.split(r'\d+', 'asj38jkas0093kjsj78kajs89==asdfj3jkkss'))

    # 6.sub(正则表达式,字符串1, 字符串2) -> 将字符串2中能够和正则表达式匹配的子串替换成字符串1，产生一个新的字符串
    print(re.sub(r'\d+', '*', 'jsj93jksj93j5a45s3s是看得见'))
    print(re.sub(r'傻逼|[傻艹草操你]', '*', '你是傻逼吗？艹!'))

    # 7.findall(正则表达式, 字符串) -> 在字符串中获取满足正则表达式的所有的子串(结果是列表)
    # 注意: 如果正则表达式中有分组，直接获取到的是分组中匹配到的内容; 如果有多个分组列表中的元素是元祖
    print(re.findall(r'\d+[a-z]', 'sjh83bkss93ksjhf9922'))
    print(re.findall(r'(\d+)[a-z]', 'sjh83bkss93=sjhf9922'))
    print(re.findall(r'abc(\d{2}|[A-Z]{2})', '=-aaabc73kkjabcKJL=3'))

    # 8.finditer(正则表达式, 字符串)  -> 在字符串中获取满足正则表达式的所有的子串(结果是迭代器,元素是匹配对象)
    result = re.finditer(r'(\d+)[a-z]', 'sj8khk83jks数据310sj=sd')
    print(result)
    print(next(result).group())

    # 9.re.I -> 忽略大小写
    # 匹配的约束条件是放在函数的flags参数中的
    print(re.fullmatch(r'[a-z]{2}', 'SA', re.I))

    # 练习
    """
    验证输入用户名和QQ号是否有效并给出对应的提示信息

    要求：
    用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
    QQ号是5~12的数字且首位不能为0
    """
    re_str1 = r'[a-zA-Z\d_]{6,20}'
    re_str2 = r'[1-9]\d{4,11}'


if __name__ == '__main__':
    test()
