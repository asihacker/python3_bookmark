class IntField:
    """
    1、实现了__get__，__set__，__delete__之一，这个类就称之为属性描述符
    属性描述符是用来统一控制属性的生成过程
    """

    def __init__(self, max_num=9, min_num=0):
        self.max_num = max_num
        self.min_num = min_num

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            if self.max_num >= value >= self.min_num:
                self.value = value
            else:
                raise ValueError("最大值：{}，最小值：{}".format(self.max_num, self.min_num))
        else:
            raise ValueError("must int value")

    def __delete__(self, instance):
        self.value = self.min_num


class NotDataField:
    """ 2、只实现一个 __get__ 被称之为非数据属性描述符 """

    def __get__(self, instance, owner):
        return 0


class User:
    age = IntField(max_num=9, min_num=1)


if __name__ == '__main__':
    """ 
    3、类的实例的__dict__，只保存实例属性
    类的__dict__，则包含类的所有属性
    """
    user = User()
    # 属性描述符的属性赋值，只是调用__set__方法
    user.age = 8
    print(user.__dict__, User.__dict__)
    # 属性描述符的属性取值，只是调用__get__方法
    print(user.age)

    """
    属性的查找顺序：
    1、如果是属性描述符，则会首先去调用属性描述符的__get__方法
    2、不是属性描述符，则会到obj.__dict__里面去找
    3、如果obj.__dict__没有，他又是非数据属性描述符，则调用非属性描述符的__get__方法
    4、如果不是非属性描述符，则去class和他的基类的__dict__里面去找
    5、都没有，执行__getattr__方法
    6、再没有，抛出属性查找不到的异常
    7`数据描述符级别>实例属性>非数据描述符
    """
