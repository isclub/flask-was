
![](https://og-image.vercel.app/**Flask**%20Was.png?theme=light&md=1&fontSize=75px&images=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fvercel-triangle-black.svg&images=https%3A%2F%2Favatars3.githubusercontent.com%2Fu%2F73245034%3Fs%3D200%26v%3D4&images=https%3A%2F%2Fflask.palletsprojects.com%2Fen%2F1.1.x%2F_static%2Fflask-icon.png&images=https%3A%2F%2Fgithub.com%2Ffluidicon.png&widths=150&heights=150)
  
🍾 **Flask extension for JSON API**


> This project is created and maintained by ISCLUB studio. Use the MIT license on GITHUB and PYPI

## Introduction

**Flask-was** can better realize the separation of front and back ends. Quickly create data verification and check before the view function runs, generate data and return. You can also create user verification functions to data verification. Fast and elegant


## Install

Use pip to install or update:

``` bash
$ pip install -U flask-was
```

## Example

**A simple Signin**

``` python
from flask import Flask
from flask_was import Was, Checker, Column

app = Flask(__name__)
api = Was(app)

api.addChecker(
    namespace="signin",
    obj=Checker(
        {
            "name": Column(api.String, biggest_str=20, smallest_str=4),
            "email": Column(api.EmailAddress, biggest_str=255, smallest_str=3),
            "password": Column(api.String, biggest_str=20, smallest_str=4),
        }
    ),
)


@app.route("/api/signin", methods=["POST"])
@api.checkeout("signin")
def api_signin(postdata):
    if postdata[0]:
        print("======== A new user coming ... ========")
        print("Name: " + postdata[1]["name"])
        print("Email: " + postdata[1]["email"])
        return api.send(json={"messagess": "Signin was OK"}, status=200)
    else:
        return api.send(
            json={"messagess": "Have some error. Check you forms", "postdata": postdata},
            status=400,
        )

app.run()
```

**Post Request**:

``` python
import requests

print(requests.post(
    "http://127.0.0.1:5000/api/signin",
    data={
        "name":"Flask",
        "email":"flask@example.org",
        "password":"12345"
    },
).text)
```

## Documentation

Read the **documentation** to get started. The documentation is in the `/docs` folder. If this project is helpful to you, please click the **Star**

## Contribution Guide

If you find errors or have good suggestions, please refer to the following template to create **issues** and **pull requests**

- `Good ideas`

``` markdown
## Introduction

What can this idea do ...

## Code

The files I changed and what did I do ...

## Info

Version Information...

Python: 3.6.x
Flask: 1.1.x
Flask-Was: 0.1.x


```

- `Problems in use`

``` markdown
## Buiness

My business needs ...

## Code

Part of the code and full traceback ...

What does my code do ...

## Info

Version Information...

Python: 3.6.x
Flask: 1.1.x
Flask-Was: 0.1.x


```

If you make a useful contribution, you will be added to the **contributors.md**

## License

**MIT LICENSE**











