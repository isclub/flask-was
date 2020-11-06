from flask_was import Checker, Column, String

register_checker = Checker({
    "username": Column(String, biggest_str=30, smallest_str=3),
    "password": Column(String, biggest_str=30, smallest_str=5)
})

get_return = register_checker.startCheck({
    "username":"flask",
    "password":123
})

if get_return:
    print(get_return)
else:
    raise ValueError("Halloween")