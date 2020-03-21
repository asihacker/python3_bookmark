#!/usr/bin/python
# coding=utf-8
import time
from functools import wraps
import threading


def check_args(func):
    @wraps(func)
    def wrapper(x, y):
        if not isinstance(x, int):
            x = int(x)
        if not isinstance(y, int):
            y = int(y)
        return func(x, y)

    return wrapper


def get_used_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        used_time = round(t2 - t1, 5)
        print(f'{func.__name__},used time is {used_time} ms')
        print(func.__doc__)
        return result

    return wrapper


@get_used_time
@check_args
def add(x, y):
    """
    hahahahahah
    :param x:
    :param y:
    :return:
    """
    print(threading.current_thread().getName())
    list = [key for key in range(100000000)]
    return x * y


@get_used_time
@check_args
def add2(x, y):
    """
    hahahahah2
    :param x:
    :param y:
    :return:
    """
    print(threading.current_thread())
    a = list()
    for key in range(100000):
        a.append(a)
    return x * y


if __name__ == '__main__':
    threading.Thread(target=add, args=[1, 1]).start()
    threading.Thread(target=add2, args=[1, 1]).start()
    print(threading.active_count())
    print(threading.activeCount())
    print(threading.enumerate())


