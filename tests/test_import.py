from flask_was import Was, Checker, Column
from flask import Flask

app = Flask(__name__)
api = Was(app)
