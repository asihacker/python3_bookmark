import datetime
from collections import namedtuple
from itertools import filterfalse

import bs4
import requests
import sympy


def demo(id: int, money: float):
    """
    打水
    :param id:
    :param money:
    :return:
    """
    PT = namedtuple('PT', ['p', 'p1', 'p2', 'time'])
    rsp = requests.get(f'http://nba.win007.com/odds/AsianOdds_n.aspx?id={id}')
    soup = bs4.BeautifulSoup(rsp.text.replace(r'<br />', '|').replace('<br>', '|'), 'html.parser')
    trs = soup.find_all('table')[1].find_all('tr')
    score = [int(k.text) for k in soup.find_all('div', class_='score')]
    c1 = []
    c2 = []
    for tr in trs[1:]:
        a = tr.find_all('td')[2].text.replace('  ', '|').strip().split('|')
        if len(a) == 3:
            a.append(datetime.datetime.strptime(tr.find_all('td')[6].text, '%Y-%m-%d %H:%M'))
            p = PT(*a)
        else:
            p = PT(p=0, p1=0, p2=0, time=datetime.datetime.strptime(tr.find_all('td')[6].text, '%Y-%m-%d %H:%M'))
        c1.append(p)
        b = tr.find_all('td')[3].text.replace('  ', '|').strip().split('|')
        if len(b) == 3:
            b.append(datetime.datetime.strptime(tr.find_all('td')[6].text, '%Y-%m-%d %H:%M'))
            p = PT(*b)
        else:
            p = PT(p=0, p1=0, p2=0, time=datetime.datetime.strptime(tr.find_all('td')[6].text, '%Y-%m-%d %H:%M'))
        c2.append(p)
    c1.reverse()
    c2.reverse()

    last = None
    for i, k in enumerate(c1):
        if k.p == 0 and last is not None:
            n_k = PT(p=last.p, p1=last.p1, p2=last.p2, time=k.time)
            c1[i] = n_k
        else:
            last = k
    last = None
    for i, k in enumerate(c2):
        if k.p == 0 and last is not None:
            n_k = PT(p=last.p, p1=last.p1, p2=last.p2, time=k.time)
            c2[i] = n_k
        else:
            last = k
    c1 = list(filterfalse(lambda x: x is None, c1))
    c2 = list(filterfalse(lambda x: x is None, c2))
    raw = 0
    for x1, x2 in zip(c1, c2):
        if all([x1.p, x2.p]) and ((float(x1.p1) + float(x2.p2)) > 2.02 or (float(x1.p2) + float(x2.p1)) > 2.02):
            if (float(x1.p1) + float(x2.p2)) > 2.02:
                p1 = float(x1.p1)
                p2 = float(x2.p2)
            else:
                p1 = float(x1.p2)
                p2 = float(x2.p1)
            # 计算金额度
            X = sympy.Symbol('X')
            Y = sympy.Symbol('Y')
            bet_m = sympy.solve([X + Y - money, X * (p1 + 1) - Y * (p2 + 1)], [X, Y])
            if score[0] > score[1] + float(x1.p):
                raw += bet_m[X] * p1 - bet_m[Y]
            else:
                raw += bet_m[Y] * p2 - bet_m[X]
            # print(score)
            # print(x1)
            # print(x2)
            # print(raw)
    return raw


def get_competition_list():
    rsp = requests.get('http://bf.win007.com/nba_date.aspx?date=2021-6-4&h=0&m=0&s=1&t=1622874876000')
    soup = bs4.BeautifulSoup(rsp.text, 'html.parser')
    return [int(k.text.split('^')[0]) for k in soup.find_all('h')]


if __name__ == '__main__':
    print(get_competition_list())
    raw_total = 0
    for k in get_competition_list():
        raw = demo(id=k, money=10000)
        raw_total += raw
        print(k, raw, raw_total)
