import time

from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {'AMQP_URI': "amqp://admin:admin@47.112.138.36"}
name = 'test'

while True:

    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning the compute task
        result = rpc.greeting_service.hello(name)
        print(result)
        result2 = rpc.greeting_service.sleep.call_async(2)
        print(result2.result())
    time.sleep(3)