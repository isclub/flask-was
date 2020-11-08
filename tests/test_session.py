from flask import Flask
from flask_was import Was, Checker, Column

def check(session,data):
    return True

def test_session():
    app = Flask(__name__)
    api = Was(app)
    api.addChecker(
        namespace="signin",
        obj=Checker(
            base={
                "name": Column(api.String, biggest_str=20, smallest_str=4),
                "email": Column(api.EmailAddress, biggest_str=255, smallest_str=20),
            },
            session=check
        ),
    )

    @app.route("/signin", methods=["GET", "POST"])
    @api.checkeout("signin")
    def client_index(postdata):
        return "Ohhhh"
