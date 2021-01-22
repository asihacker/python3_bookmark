import json

import requests


def cookie_to_dict(cookie: str):
    """
    把文本cookie转化为dict
    """
    ck_list = [k.split('=') for k in cookie.split('; ')]
    ck_dict = {k[0]: k[1] for k in ck_list}
    return ck_dict


# url = "http://www.okooo.com/soccer/match/1123586/odds/ajax/?page=0&trnum=0&companytype=BaijiaBooks&type=0"
#
# payload = {}
# headers = {}
# cookies = cookie_to_dict("LastUrl=; PHPSESSID=5d728ec6ec89fc5af166dfc8531938b18a426063; __utmc=56961525; __utmz=56961525.1610511277.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_5ffc07c2ca2eda4cc1c4d8e50804c94b=1610511277; pm=; IMUserID=31032919; IMUserName=%E5%93%88%E7%BB%B4392687; OKSID=5d728ec6ec89fc5af166dfc8531938b18a426063; M_UserName=%22%5Cu54c8%5Cu7ef4392687%22; M_UserID=31032919; M_Ukey=d8e12329d81b851763dd6074e5fae147; OkAutoUuid=910a03c8c22aea0b67a76ec59a94e49d; OkMsIndex=2; FirstURL=www.okooo.com/soccer/match/1123586/odds/; FirstOKURL=http%3A//www.okooo.com/soccer/match/1123586/odds/change/24/; First_Source=www.okooo.com; acw_tc=2f624a5a16105458495213587e4204aa44072b6c465d9088c599bd12ccab31; __utma=56961525.1120291333.1610511277.1610540729.1610545850.7; Hm_lpvt_5ffc07c2ca2eda4cc1c4d8e50804c94b=1610546127; __utmb=56961525.11.9.1610546127252")
# print(json.dumps(cookies))
# session = requests.session()
# session.headers.update({
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'})
# session.headers.update({'Accept-Encoding': 'gzip, deflate'})
# session.headers.update({'Accept-Language': 'zh-CN,zh;q=0.9'})
# # session.headers.update({'Accept': 'text/html, */*'})
# # session.headers.update({'Referer': 'http://www.okooo.com/soccer/match/1123586/odds/'})
# # session.cookies.update(cookies)
# response = session.request("GET", url, headers=headers, data=payload)
# print(response.status_code, response.cookies.get_dict())
# response = session.request("GET", url, headers=headers, data=payload)
# print(response.status_code, response.cookies.get_dict())
# print(response.status_code)
# if response.status_code == 200:
#     print(response.text)
if __name__ == '__main__':
    import json
    print(json.dumps(cookie_to_dict("LastUrl=; PHPSESSID=5d728ec6ec89fc5af166dfc8531938b18a426063; __utmc=56961525; __utmz=56961525.1610511277.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_5ffc07c2ca2eda4cc1c4d8e50804c94b=1610511277; pm=; IMUserID=31032919; IMUserName=%E5%93%88%E7%BB%B4392687; OKSID=5d728ec6ec89fc5af166dfc8531938b18a426063; M_UserName=%22%5Cu54c8%5Cu7ef4392687%22; M_UserID=31032919; M_Ukey=d8e12329d81b851763dd6074e5fae147; OkAutoUuid=910a03c8c22aea0b67a76ec59a94e49d; OkMsIndex=2; FirstURL=www.okooo.com/soccer/match/1123586/odds/; FirstOKURL=http%3A//www.okooo.com/soccer/match/1123586/odds/change/24/; First_Source=www.okooo.com; __utma=56961525.1120291333.1610511277.1610596385.1610608530.9; acw_tc=2f624a5716106085303998865e6a312157e9266dc99611ed53179c7dee9c58; Hm_lpvt_5ffc07c2ca2eda4cc1c4d8e50804c94b=1610608637; __utmb=56961525.8.9.1610608637253")))