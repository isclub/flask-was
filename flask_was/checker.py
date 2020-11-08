from flask import session

class Checker(object):
    def __init__(self, base={},session=None):
        self.base = base
        self.session = session

    def startCheck(self, obj):
        for nowColumnName in self.base:
            try:
                obj[nowColumnName]
            except:
                return [False, nowColumnName, "miss", obj]
        for nowColumn in obj:
            if (len(str(obj[nowColumn])) < self.base[nowColumn].smallest_str) or (
                len(str(obj[nowColumn])) > self.base[nowColumn].biggest_str
            ):
                return [False, nowColumn, "length", obj]
            if not self.base[nowColumn].checktype_func(obj[nowColumn]):
                return [False, nowColumn, "type", obj]
        session_dispatch = self.session(session=session,data=obj)
        if session_dispatch:
            return [True,obj]
        else:
            return [False,"","session",obj]


class Column(object):
    def __init__(self, checktype_func, biggest_str=25565, smallest_str=0):
        self.checktype_func = checktype_func
        self.biggest_str = biggest_str
        self.smallest_str = smallest_str


__all__ = ["Checker", "Column"]
