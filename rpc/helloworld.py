import time

from nameko.rpc import rpc


class GreetingService:
    name = "greeting_service"
    i = 6

    @rpc
    def hello(self, name):
        return "hello, {}!".format(name) + str(self.i)

    @rpc
    def sleep(self, second: int):
        time.sleep(second)
        return 'done' + str(self.i)
