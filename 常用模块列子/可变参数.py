def add(x: int, y: int):  # 默认参数
    print(x, y)
    return x + y


def add2(*x):  # 可变参数
    print(x)
    return


def add3(**kwargs):  # 关键字参数
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
    for i, k in enumerate(kwargs):
        print(i, k)
    for i, k in enumerate(kwargs.items()):
        print(i, k)
    return


def add4(*args, **kwargs):  # 可变参数和关键词参数
    print(args, kwargs)
    return


if __name__ == '__main__':
    add(1, 2)
    add2(1, 2, 3, 4, 5, 6)
    add3(a=1, b=2, c=3, d=4)
    add4(2, 4, 5, 6, 7, a=1, b=2, c=3, d=4)
