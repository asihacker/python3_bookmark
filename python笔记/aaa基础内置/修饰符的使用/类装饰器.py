#!/usr/bin/python
# coding=utf-8
import time
from functools import wraps


# https://www.zhangshengrong.com/p/8AaY32blX2/

class check_args(object):
    """
    用于检查参数是否存在
    """

    def __init__(self, **kwargs):
        self.requests_args = kwargs.get('requests_args', [])

    def __call__(self, func):  # 接受函数
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{func.__name__}')
            for arg in self.requests_args:
                if arg not in kwargs:
                    return f'缺少必要参数{arg}'
            return func(*args, **kwargs)

        return wrapper  # 返回函数


class check_time(object):
    # def __init__(self):
    #     pass

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            print(round(time.time() - t0, 2))
            return result

        return wrapper


@check_args(requests_args=['bet', 'b', 'c'])
@check_time()
def ayy(*args, **kwargs):
    print(ayy.__name__)
    time.sleep(3)
    return 'ok'


if __name__ == '__main__':
    print(ayy(1, 2, 3, a=22, c=1, b=3))
