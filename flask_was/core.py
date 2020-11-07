from flask import current_app, _app_ctx_stack

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

    def init_app(self, app):
        app.config.setdefault("WASAPI_FORMAT", True)
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top


__all__ = ["Was"]
