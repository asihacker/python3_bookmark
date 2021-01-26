import json


def cookie_to_dict(cookie: str):
    """
    把文本cookie转化为dict
    """
    ck_list = [k.split('=') for k in cookie.split('; ')]
    ck_dict = {k[0]: k[1] for k in ck_list}
    print(json.dumps(ck_dict))
    return ck_dict

if __name__ == '__main__':
    cookie_to_dict('ASP.NET_SessionId=oizgeg1jb4mlrdxkei0kr4vx; lobbyUrl=#; settingProfile=OddsType=2&NoOfLinePerEvent=1&SortBy=1&AutoRefreshBetslip=False; fav3=; favByBetType=; fav-com=; CCDefaultTvPlay=; CCDefaultBgPlay=; redirect=done; lan=zh-cn; dangerStatus=%7B%22t%22%3A%5B%7B%22bid%22%3A%2287144317670170%22%2C%22ts%22%3A1%2C%22bi%22%3A%5B%7B%22did%22%3A%22139850679%22%2C%22bis%22%3A1%7D%5D%7D%5D%2C%22f%22%3Atrue%2C%22rc%22%3A0%7D; spitok=jPlVOBBiQBcm%2Fo%2BIcbrZe8EOLWdvw9Xb8AnRkE9J8z%2BsSHJ2GnLvvkYyAqUVk6Xb; logoutUrl=https://www.yabo829.com; historyUrl=%2Fm%2Fzh-cn%2Fsports%2Ffootball%2Fselect-competition%2Fdefault%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2Ffootball%2Fin-play%2Ffull-time-asian-handicap-and-over-under%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2F4628673%2Fin-play%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2Ffootball%2Fselect-competition%2Fdefault%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2Ffootball%2Fin-play%2Ffull-time-asian-handicap-and-over-under%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2Ffootball%2Fselect-competition%2Fdefault%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2Fbasketball%2Fin-play%2Ffull-time-asian-handicap-and-over-under%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2Ffootball%2Fin-play%2Ffull-time-asian-handicap-and-over-under%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2Ffootball%2Fselect-competition%2Fdefault%3Fsc%3DABHAJG%26theme%3DYABO%7C%2Fm%2Fzh-cn%2Fsports%2Ffootball%2Fin-play%2Ffull-time-asian-handicap-and-over-under%3Fsc%3DABHAJG%26theme%3DYABO; timeZone=480; sbmwl3-yabo=1578176266.20480.0000; opCode=YABO; BS@Cookies=5685848241%234621080%230%23true%23%231.01%23null%233%3A1%23true%23true%23%234621080%23false%23; mc=WL67Amoney888go')