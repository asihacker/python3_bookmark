import requests
import json

url = "https://www.6004yb.com/api/site/group/account/memberLogin/v3/login"

payload = json.dumps({
  "xx": "dlYAE4IITwEl6YTQshT0c/kq8GZBN2vYgX1TWnW4WDw1l/GKld16V6NDiQg/SnOy1p3HvMhlOxlfzcJaQ94KLvLOMdLz4LfsCipgn7wjw23eg5i/i0gWFfOL04lyPmzAmojXoCVNzGCpvlXZh7JKgCGfKygKSct7I6zG1VhxuGq9zQKZiBZwJfLjDK5x9Av9pvUs3UY8vV3pt/XkSw0wsg=="
})
headers = {
  'Accept': '*/*',
  'CTBDQ': 'NDbTd5RysclL',
  'Connection': 'keep-alive',
  'Content-Length': '216',
  # 'Cookie': 'asihk888=cjx6089229; timeZone=480; acw_tc=ac11000116176907231293593e0124a6e4609c23809f58dadbdd4cd5e99ea5; waf_cookie=4ac5e5b0-e6dd-4fcb2800db6513ac5bdb9a44616e9d45f481',
  'DSRVY': 'mPLK3Ic7GzdXXOIquU1QSqs0sjUFhx5U',
  'FUQVA': 'v1.0.1',
  'HRHKP': '0CbXb0XcBPH3URdl',
  'NLGFN': '7B503FB8-BDF6-4CEC-BBE7-3276411F7EED',
  'QJZDV': '2',
  'RWNAV': '',
  'SKKTW': 'h5',
  'TULSY': '1617690790',
  'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo Xplay6 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.8.5.1065 Mobile Safari/537.36',
  'XGHBQ': 'eebb3e64f3ea51430cb974b1d553ada585085751',
  'YUJFQ': 'h5',
  'authority': 'www.6004yb.com',
  'content-type': 'application/json',
  'origin': 'https://www.6004yb.com',
  'referer': 'https://www.6004yb.com/entry/login'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
