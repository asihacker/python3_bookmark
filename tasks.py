from fake_useragent import UserAgent

ua = UserAgent()
for _ in range(10100):
    print(ua.chrome)