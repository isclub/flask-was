import json
import re

"""
from flask_was import Checker, Column, String

register_checker = Checker({
    "username": Column(String, biggest_str=30, smallest_str=3),
    "password": Column(String, biggest_str=30, smallest_str=5)
})
"""


class Checker(object):
    def __init__(self, base={}):
        self.base = {}

    def startCheck(self, obj):
        for nowColumn in self.base:
            if (len(obj) < self.base[nowColumn].smallest_str) or (
                len(obj) > self.base[nowColumn].biggest_str
            ):
                return [False, nowColumn]
            if not self.base[nowColumn].checktype_func(obj):
                return [False, nowColumn]
        return [True]


class Column(object):
    def __init__(self, checktype_func, biggest_str=0, smallest_str=0):
        self.checktype_func = checktype_func
        self.biggest_str = biggest_str
        self.smallest_str = smallest_str
