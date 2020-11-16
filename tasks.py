class Apple(object):
    def get_max(self, a: int, b: int):
        return max(a, b)

    def __get_max(self, a: int, b: int):
        return a + b

    def fuck(self):
        return

    def _fuck2(self):
        return

    def __fuck3(self):
        return


a = Apple()

print(a.get_max(1, 3))
print(a.get_max(4, 4))
print(dir(Apple))
