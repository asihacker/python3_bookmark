import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor


def test2():
    time.sleep(5)
    print(111)


def test():
    with ThreadPoolExecutor(max_workers=1) as t:
        obj = t.submit(test2)
        print(obj.done())
        print(obj.result())
        print(obj.done())
    print(222)


if __name__ == '__main__':
    test()
