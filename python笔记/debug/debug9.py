class Apple:
    a = 10

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def test(self):
        print(sum([self.b, self.b]))

    def send_msg(self):
        pass

    def handler(self):
        def inner(func):
            self.call = func
            print('注册回调函数')
            return func

        return inner

    def __getattribute__(self, item):
        obj = object.__getattribute__(self, item)
        print(type(obj), obj)
        return obj


a = Apple(a=15, b=20)
print(a.a)
print(a.b)
a.test()


@a.handler()
def job(msg):
    print('收到消息', msg)
