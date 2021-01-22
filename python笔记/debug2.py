import json
import time

import requests


def login_okooo(username: str, password: str):
    """
    登录okooo
    :param username:
    :param password:
    :return:
    """
    captcha_url = f"http://account.okooo.com/api/?method=api.account.captcha.get&format=jsonp&jsoncallback=_jqjsp&_{int(time.time() * 1000)}="
    session = requests.session()
    rsp = session.get(captcha_url)
    img = json.loads(rsp.text.replace('_jqjsp(', '').replace(')', ''))['data']['img'].replace('data:image/jpeg;base64,',
                                                                                              '')
    data = {"username": 'asihacker', "password": 'i5D84.JYnXes', "image": img}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if not result['success']:
        raise BaseException('验证码识别接口错误' + result["message"])
    else:
        captcha = result["data"]["result"]
        check_captcha_url = f'http://account.okooo.com/api/?method=api.account.captcha.check&captcha={captcha}&status=on&format=jsonp&jsoncallback=_jqjsp&_{int(time.time() * 1000)}='
        rsp = session.get(check_captcha_url)
        result = json.loads(rsp.text.replace('_jqjsp(', '').replace(')', ''))
        if result['code'] == 1000:
            login_url = f'http://account.okooo.com/api/?source=1&method=api.account.auth.login&user_name={username}&password={password}&captcha={captcha}&is_remember=1&format=jsonp&jsoncallback=_jqjsp&_{int(time.time() * 1000)}='
            rsp = session.get(login_url)
            result = json.loads(rsp.text.replace('_jqjsp(', '').replace(')', ''))
            if result['code'] == 1000:
                return json.dumps(session.cookies.get_dict())
            else:
                raise BaseException(result['msg'])
        else:
            raise BaseException('验证码识别错误' + result['msg'])


if __name__ == '__main__':
    """
    ok_502898784660+football888
    ok_580672199243+football888
    ok_002233193500+football888
    ok_030721738225+football888
    wx_343324817+football888
    ok_032910977772+football888
    ok_313051474722+football888
    ok_315099223548+football888
    ok_355798464616+ football888
    ok_385509750700+football888
    """
    print(login_okooo('ok_502898784660', 'football888'))
    # print(login('18970084363', 'nantian888'))
