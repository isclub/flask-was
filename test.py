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
