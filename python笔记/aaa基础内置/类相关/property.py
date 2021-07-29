class Apple:
    """
    debug
    """

    def __init__(self):
        self._age = None

    @property
    def age(self):
        """

        :return:
        """
        return self._age

    @age.getter
    def age(self):
        """

        :return:
        """
        print('我被调用了getter')
        # return f'{self._age}是我的年龄'
        return self._age

    @age.setter
    def age(self, value):
        """

        :param value:
        :return:
        """
        print('我被调用了setter')
        if isinstance(value, int):
            self._age = value
            return
        else:
            raise ValueError('age 必须为int类型')


a = Apple()
a.age = '123'
print(a.age)
