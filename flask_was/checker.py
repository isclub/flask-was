class Checker(object):
    def __init__(self, base={}):
        self.base = base

    def startCheck(self, obj):
        for nowColumnName in self.base:
            try:
                obj[nowColumnName]
            except:
                return [False, nowColumnName, "miss"]
        for nowColumn in obj:
            if (len(str(obj)) < self.base[nowColumn].smallest_str) or (
                len(str(obj)) > self.base[nowColumn].biggest_str
            ):
                return [False, nowColumn, "length"]
            if self.base[nowColumn].checktype_func(obj) != True:
                return [False, nowColumn, "type"]
        return [True]


class Column(object):
    def __init__(self, checktype_func, biggest_str=25565, smallest_str=0):
        self.checktype_func = checktype_func
        self.biggest_str = biggest_str
        self.smallest_str = smallest_str


__all__ = ["Checker", "Column"]