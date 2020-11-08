![](https://og-image.vercel.app/**Flask**%20Was.png?theme=light&md=1&fontSize=75px&images=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fvercel-triangle-black.svg&images=https%3A%2F%2Favatars3.githubusercontent.com%2Fu%2F73245034%3Fs%3D200%26v%3D4&images=https%3A%2F%2Fflask.palletsprojects.com%2Fen%2F1.1.x%2F_static%2Fflask-icon.png&images=https%3A%2F%2Fgithub.com%2Ffluidicon.png&widths=150&heights=150)

🍾 **JSON API 的 Flask 扩展**

[English](README.md "English Version")

> 该项目由 ISCLUB Studio 创建和维护。在 GITHUB 和 PYPI 上使用 MIT 许可证开源。

## 介绍

**Flask-was** 可以更好地实现前端和后端的分离，在视图函数运行、生成数据和返回之前快速创建数据验证和检查，您还可以创建用户验证功能以进行数据验证。快速、优雅！


## 安装

使用 pip 安装或升级:

``` bash
$ pip install -U flask-was
```

## 示例

**简单的登录示例**

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
        return api.send(json={"messages": "Signin was OK"}, status=200)
    else:
        return api.send(
            json={"messages": "Have some error. Check you forms", "postdata": postdata},
            status=400,
        )

app.run()
```

**发送请求**:

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

## 文档

请阅读**文档**以开始使用，文档位于 `/docs` 文件夹中。如果这个项目对您有帮助，请点击 `Star`.

## 贡献指南

如果您发现错误或有好的建议，请参阅以下模板以创建[**议题**](https://github.com/isclub/flask-was/issues "Issues")和[**拉取请求**](https://github.com/isclub/flask-was/pulls "Pull Requests")。

- `好的想法`

``` markdown
## 介绍

这个想法有什么用……

## 代码

我更改的文件和尝试进行的操作……

## 信息

版本信息……

Python: 3.6.x
Flask: 1.1.x
Flask-Was: 0.1.x

```

- `使用中的问题`

``` markdown
## 预期

我的业务需要……

## 代码

代码和完整回溯的一部分……

我的代码发生什么了……

## 信息

版本信息……

Python: 3.6.x
Flask: 1.1.x
Flask-Was: 0.1.x

```

如果您做出了有益的贡献，您将被添加到 **contributors.md**.

## 许可证

**MIT LICENSE**