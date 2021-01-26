#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 18:33
# @Author  : AsiHacker
# @File    : debug3.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import base64
import hashlib
import hmac
import random
import string
import time
from hashlib import sha256

import requests


def get_nonce_str():
    """

    :return:
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))


def get_password(name: str, password: str):
    """
    密码加密
    :param name:
    :param password:
    :return:
    """
    c = hashlib.md5(name.encode()).hexdigest()[2:17]
    a: str = f'{c}{password}{c}'
    return hashlib.md5(a.encode()).hexdigest()


def get_sign(params: dict, key: str = 'c47297f9e0fe99ef289ae514b96bd34b'):
    """

    :param params: 参数字典
    :param key: 密钥
    :return:
    """

    params_list = [f'{value}={params[value]}' for value in sorted([key for key in params]) if
                   isinstance(params[value], str) and params[value]]
    params_list.append(f'appSecurit={key}')
    da = '&'.join(params_list)
    da_base64 = base64.b64encode(da.encode())
    return hmac.new(key.encode('utf-8'), da_base64, digestmod=sha256).hexdigest()


def get_uuid():
    """
    获取uuid
    :return:
    """
    return f'h5-android-{hashlib.md5(get_nonce_str().encode()).hexdigest()}'


def login(name: str, password: str):
    """
    登录下单平台
    :param name:
    :param password:
    :return:
    """
    session = requests.session()
    session.cookies.set('timeZone', '480')
    session.cookies.set(name, password)
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'})

    post_data = {
        'uuid': get_uuid(),
        'name': name,
        'password': get_password(name, password),
        'domain': 'www.yabo416.com',
        'type': '1',
        'appKey': '249aaea6de9a2e00c1',
        'timestamp': str(int(time.time())),
        'nonce_str': get_nonce_str(),
    }
    sign = get_sign(params=post_data)
    post_data.update({'sign': sign})
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'cache-control': 'no-cache',
        'client-type': 'h5',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.yabo416.com',
        'referer': 'https://www.yabo416.com/entry/login',
    }
    session.headers.update(headers)
    rsp = session.post('https://www.yabo416.com/member/v2/web_login', data=post_data)
    print(rsp.json())
    session.headers.update({'x-api-token': rsp.json()['data']['token']})
    post_data_launch = {
        'api_name': 'SPORT',
        'is_app': '',
        'https': True,
        'appKey': '249aaea6de9a2e00c1',
        'timestamp': str(int(time.time())),
        'nonce_str': get_nonce_str(),
    }
    sign = get_sign(params=post_data_launch)
    post_data_launch.update({'sign': sign})
    rsp = session.post('https://www.yabo416.com/cg/v1/game/sport/launch', data=post_data_launch)
    # launch
    url = rsp.json()['data']['html']
    print(">>>>>>>>", url)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Host': 'xj-mbs-yabo.q8825h.com',
        'Referer': 'https://www.yabo416.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
    }
    session.headers.update(headers)
    rsp = session.get(url)
    print(rsp.cookies.get_dict())
    session.cookies.update(rsp.cookies.get_dict())
    print(session.cookies.get_dict())
    headers = {
        'Host': 'xj-mbs-yabo.q8825h.com',
        'Referer': url,
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
    }
    session.headers.update(headers)
    rsp = session.get(url)
    print(rsp.cookies.get_dict())
    session.cookies.update(rsp.cookies.get_dict())
    print(session.cookies.get_dict())
    # print(rsp.json())
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://xj-mbs-yabo.q8825h.com',
        'Referer': 'https://xj-mbs-yabo.q8825h.com/m/zh-cn/sports/?sc=ABHAIB&theme=YABO',
    }
    session.headers.update(headers)
    rsp = session.post(
        f'https://xj-mbs-yabo.q8825h.com/zh-cn/Service/UserService?UpdateBalance&ts={int(time.time() * 1000)}',
        data={})
    print(rsp.text)
    # 查询余额
    post_data2 = {
        'IsFirstLoad': True,
        'VersionH': 0,
        'IsEventMenu': False,
        'SportID': 1,
        'CompetitionID': -1,
        # 'reqUrl': '/m/zh-cn/sports/football/select-competition/default?date=today',
        'reqUrl': '/m/zh-cn/sports/football/in-play/full-time-asian-handicap-and-over-under?sc=ABHAJG&theme=YABO',
        'IsMobile': True,
        'oCompetitionId': 0,
        'oEventIds': 0,
        'oIsFirstLoad': True,
        'oPageNo': 0,
        'oSortBy': 1,
        'LiveCenterEventId': 0,
        'LiveCenterSportId': 1,
    }
    rsp = session.post(
        f'https://xj-mbs-yabo.q8825h.com/zh-cn/Service/CentralService?GetData&ts={int(time.time() * 1000)}',
        data=post_data2)
    # # 获取今日赛事
    # # for index, key in enumerate(rsp.json()['lpd']['psm']['psmd'][0]['puc']):
    # #     year = datetime.datetime.now().strftime('%Y') + '-'
    # #     mark = datetime.datetime.now().replace(hour=0, minute=0, second=0)
    # #     today = mark + datetime.timedelta(hours=12)
    # #     tomorrow = (mark + datetime.timedelta(days=1) + datetime.timedelta(hours=12))
    # #     for i, k in enumerate(key['ces']):
    # #         if k['ht'] == '埃斯蒂特斯卡塞罗斯':
    # #             print(2)
    # #             pass
    # #         day = k['esd']
    # #         hour = k['est']
    # #         start_time = ''.join([year, day, hour])
    # #         start_time = datetime.datetime.strptime(start_time, '%Y-%m月%d日%H:%M')
    # #         if today <= start_time <= tomorrow:
    # #             print('🔥', k['eid'], k['ht'], k['at'], k['esd'], k['est'], start_time, sep='\t')
    # #         else:
    # #             print('⌚️', k['eid'], k['ht'], k['at'], k['esd'], k['est'], start_time, sep='\t')
    # 下单
    for index, key in enumerate(rsp.json()['mod']['d'][0]['c']):
        league = key['n']
        print(league)
        for i, k in enumerate(key['e']):
            if '1x2' in k['o']:
                print('>>>', k['pk'], k['i'][0], k['i'][1], k['o']['1x2'], k['i'][10], k['i'][11], sep='\t')
                if k['i'][0] == '悉尼':
                    cc = {
                        k['o']['1x2'][0]: k['o']['1x2'][1],
                        k['o']['1x2'][2]: k['o']['1x2'][3],
                        k['o']['1x2'][4]: k['o']['1x2'][5],
                    }
                    print(cc)
                    odds = k['o']['1x2'][1]
                    direction = k['o']['1x2'][0][1:]
                    score_h = k['i'][10]
                    score_a = k['i'][11]
                    rmb = 10
                    pk = k['pk']
                    SingleList = f'{direction}@{odds}@null@{score_h}:{score_a}@{rmb}@true@{odds}@{pk}@true@{pk}@false'
                    post_data3 = {
                        'SingleList': f'{direction}@{odds}@null@{score_h}:{score_a}@{rmb}@true@{odds}@{pk}@true@{pk}@false',
                        'ComboList': '',
                        'NoOfCombine': 1,
                        'source': 8,
                    }
                    # post_data3 = f'SingleList={SingleList}&ComboList=&NoOfCombine=1&source=8'
                    print('下单参数》》》》》', post_data3)
                    headers = {
                        'Accept': '*/*',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'origin': 'https://xj-mbs-yabo.q8825h.com',
                        'Pragma': 'no-cache',
                        'Referer': 'https://xj-mbs-yabo.q8825h.com/m/zh-cn/sports/football/in-play/full-time-asian-handicap-and-over-under?sc=ABHAJG&theme=YABO',
                    }
                    session.headers.update(headers)
                    rsp = session.post(
                        f'https://xj-mbs-yabo.q8825h.com/zh-cn/Service/BetSlipService?PlaceBetNew&ts={int(time.time() * 1000)}',
                        data=post_data3)
                    print(rsp.json())
                    exit()


if __name__ == '__main__':
    login(name='money888go', password='wahaha82')
    # login(name='asihacker1', password='nantian888')
    # da = f'api=SPORT&appKey=249aaea6de9a2e00c1&nonce_str=ou8fk0e31rp&timestamp=1611230031&appSecurit=c47297f9e0fe99ef289ae514b96bd34b'
