class FberrorMsg(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return '卧槽小陈错误'


raise FberrorMsg
