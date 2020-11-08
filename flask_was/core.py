from flask import current_app, _app_ctx_stack, request, sessions, Response
from functools import wraps

from .items import (
    String,
    Number,
    List,
    Dict,
    WeChatID,
    TencentQQID,
    PhoneID,
    ChinaPhoneID,
    CardID,
    ChinaPostID,
    InternetProtocolAddress,
    URLAddress,
    EmailAddress,
    ChineseOhhhYeah,
)

from .checker import Checker


class Was(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

        self.String = String
        self.Number = Number
        self.List = List
        self.Dict = Dict
        self.WeChatID = WeChatID
        self.TencentQQID = TencentQQID
        self.PhoneId = PhoneID
        self.ChinaPhoneID = ChinaPhoneID
        self.CardID = CardID
        self.ChinaPostID = ChinaPostID
        self.InternetProtocolAddress = InternetProtocolAddress
        self.URLAddress = URLAddress
        self.EmailAddress = EmailAddress
        self.ChineseOhhhYeah = ChineseOhhhYeah

        self.checker = {}

    def init_app(self, app):
        app.config.setdefault("WASAPI_FORMAT", True)
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top

    def handlerPost(self, checker):
        try:
            self.checker[checker]
        except:
            raise RuntimeError("Can find Checker.")
        data = request.form
        overdata = self.checker[checker].startCheck(data)
        return overdata

    def addChecker(self, namespace, obj):
        if not isinstance(obj, Checker):
            raise TypeError("Only Checker objects can be added.")
        self.checker[namespace] = obj

    def checkeout(self, hanlderChecker):
        def decorator(f):
            def handler(*args, **kwargs):
                print("a")
                handlerPost = self.handlerPost(hanlderChecker)
                return f(*((handlerPost,) + args), **kwargs)

            return handler

        return decorator

    def send(self, json={}, status=200):
        return Response(
            response=str(json), status=status, content_type="application/json"
        )


__all__ = ["Was"]
