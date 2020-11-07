import re


# Basic Items


def String(obj):
    return type(obj) == str


def Number(obj):
    return type(obj) == int


def List(obj):
    return type(obj) == list


def Dict(obj):
    return type(obj) == dict


# ID Items


def WeChatID(obj):
    return re.compile(r"^[a-zA-Z]{1}[-_a-zA-Z0-9]{5,19}$").match(obj)


def TencentQQID(obj):
    return re.compile(r"[1-9][0-9]{4,}").match(obj)


def PhoneID(obj):
    return re.compile(r"^1[34578]\d{9}$").match(obj)


def ChinaPhoneID(obj):
    return re.compile(r"\d{3}-\d{8}|\d{4}-\{7,8}").match(obj)


def CardID(obj):
    return re.compile(r"^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X|x)$").match(obj)


def ChinaPostID(obj):
    return re.compile(r"[1-9]\d{5}(?!\d)").match(obj)


# Address Items


def InternetProtocolAddress(obj):
    return re.compile(
        r"(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d).(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d).(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d).(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
    ).match(obj)


def URLAddress(obj):
    return re.compile(r"[a-zA-z]+://[^\s]*").match(obj)


def EmailAddress(obj):
    return re.compile(
        r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
    ).match(obj)


# Other Items


def ChineseOhhhYeah(obj):
    return re.compile("[\u4e00-\u9fa5]").match(obj)


__all__ = [
    "String",
    "Number",
    "List",
    "Dict",
    "WeChatID",
    "TencentQQID",
    "PhoneID",
    "ChinaPhoneID",
    "CardID",
    "ChinaPostID",
    "InternetProtocolAddress",
    "URLAddress",
    "EmailAddress",
    "ChineseOhhhYeah",
]
