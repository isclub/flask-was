# Flask-Was
🎨 The API extension of the flask is very comfortable and good

## Feature

- Out of the box, easy to use
- Quick definition of inspection model
- Fast data model
- Convert data to objects
- Friendly user authentication

## Install

Use pip to install or update:

``` bash
pip install -U flask-was
```

## Usage

A Simple Checker:

``` python
from flask_was import Checker, Column, String

register_checker = Checker({
    "username": Column(String, biggest_str=30, smallest_str=3),
    "password": Column(String, biggest_str=30, smallest_str=5)
})

get_return = register_checker.startCheck({
    "username":"flask",
    "password":"12345678"
})
print(get_return)
```

It's output:

``` python
[True]
```
