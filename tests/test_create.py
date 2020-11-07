from flask import Flask
from flask_was import Was, Checker, Column


def test_createapp():
    app = Flask(__name__)
    api = Was(app)
    return api


def test_createchecker():
    api = test_createapp()
    test = Checker({"name": Column(api.String)})


def test_createchecker_manycolumn():
    api = test_createapp()
    test = Checker(
        {
            "name": Column(api.String),
            "email": Column(api.EmailAddress),
            "password": Column(api.String),
        }
    )


def test_createchecker_setest():
    api = test_createapp()
    test = Checker({"name": Column(api.String, biggest_str=25565, smallest_str=0)})


def test_createchecker_addtoapp():
    api = test_createapp()
    test = Checker(
        {
            "name": Column(api.String),
            "email": Column(api.EmailAddress),
            "password": Column(api.String),
        }
    )
    api.addChecker("test", test)
