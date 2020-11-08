# Flask-Was

Welcome to this **Quick Start** to learn how to use it. You can also read the detailed API reference below

## Install

Use pip to install or update:

``` bash
$ pip install -U flask-was
```

Download the latest version using GitHub:

``` bash
$ git clone https://github.com/isclub/flask-was
$ cd flask-was
$ python setup.py install
```

## Bind

Add extension to app

``` python
from flask import Flask
from flask_was import Was

app = Flask(__name__)
api = Was(app)
```

## Checker

Create a checker

``` python
from flask import Flask
from flask_was import Was, Checker, Column


app = Flask(__name__)
api = Was(app)

check = Checker({"name": Column(api.String)})
```

## Column

Set a Column

``` python
from flask import Flask
from flask_was import Was, Checker, Column

app = Flask(__name__)
api = Was(app)

Column(api.String,biggest_str=25565,smaller_str=0)
```

## Check Value

Check value

``` python
from flask import Flask
from flask_was import Was, Checker, Column

app = Flask(__name__)
api = Was(app)

Column(api.String)
Column(api.Number)
Column(api.List)
Column(api.Dict)
```

> More check functions? Please go to API reference

## Add Checker

Add the check to the application to call

``` python
from flask import Flask
from flask_was import Was, Checker, Column

app = Flask(__name__)
api = Was(app)

test = Checker({
    "name": Column(api.String),
    "email": Column(api.EmailAddress),
    "password": Column(api.String)})
api.addChecker("test", test)
```

## Use in view-func

Use in view functions

``` python
from flask import Flask
from flask_was import Was, Checker, Column

app = Flask(__name__)
api = Was(app)

test = Checker({
    "name": Column(api.String),
    "email": Column(api.EmailAddress),
    "password": Column(api.String)})
api.addChecker("test", test)

@app.route("/api/test", methods=["POST"])
@api.checkeout("test")
def client_index(postdata):
    return "Hello"
```

## PostData

Results of inspection

``` python

Use in view functions

``` python
from flask import Flask
from flask_was import Was, Checker, Column

app = Flask(__name__)
api = Was(app)

test = Checker({
    "name": Column(api.String),
    "email": Column(api.EmailAddress),
    "password": Column(api.String)})
api.addChecker("test", test)

@app.route("/api/test", methods=["POST"])
@api.checkeout("test")
def client_index(postdata):
    postdata[0]
    # True or False

    postdata[1]
    # Error Column

    postdata[2]
    # Cause of error

    postdata[3]
    # Client data

    return "Hello"
```

## Session

Custom functions to check, for example, to verify the user's identity

``` python
from flask import Flask
from flask_was import Was, Checker, Column

app = Flask(__name__)
api = Was(app)

def check_status(session,data):
    # My Check Function ...
    # Return True or False ...
    return True

test = Checker({
    "name": Column(api.String),
    "email": Column(api.EmailAddress),
    "password": Column(api.String)},check_status)
api.addChecker("test", test)

@app.route("/api/test", methods=["POST"])
@api.checkeout("test")
def client_index(postdata):
    return "Hello"
```

## Send

Send data to client

``` python
from flask import Flask
from flask_was import Was, Checker, Column

app = Flask(__name__)
api = Was(app)

def check_status(session,data):
    # My Check Function ...
    # Return True or False ...
    return True

test = Checker({
    "name": Column(api.String),
    "email": Column(api.EmailAddress),
    "password": Column(api.String)},check_status)
api.addChecker("test", test)

@app.route("/api/test", methods=["POST"])
@api.checkeout("test")
def client_index(postdata):
    return api.send(
        json={},
        status=200
    )
```

## API Reference

``` python

# All Value-Checker
[
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

# Core Object
class Was(object):
    def __init__(self,app=None):
        # app = Flask(__name__)
        # api = Was(app)
    
    def addChecker(self, namespace, obj): 
        # test = Checker({
        #   "name": Column(api.String),
        #   "email": Column(api.EmailAddress),
        #   "password": Column(api.String)
        # })
        # api.addChecker("test", test)

    def checkeout(self, hanlderChecker):
        # @app.route("/api/test", methods=["POST"])
        # @api.checkeout("test")
        # def client_index(postdata):
        # return "Hello"
    
    def send(self, json={}, status=200):
        # @app.route("/api/test", methods=["POST"])
        # @api.checkeout("test")
        # def client_index(postdata):
        # return api.send(
        #   json={},
        #   status=200
        # )


# Checker Object
class Checker(object):
    def __init__(self, base={},session=None):
        # Checker({
        #   "name": Column(api.String),
        #   "email": Column(api.EmailAddress),
        #   "password": Column(api.String)
        # })

# Column Object
class Column(object):
    def __init__(self, checktype_func, biggest_str=25565, smallest_str=0):
        # Column(
        #   api.String,
        #   biggest_str=25565, 
        #   smallest_str=0
        # )

__all__ = [
    "Was",
    "Checker",
    "Column",
]
```