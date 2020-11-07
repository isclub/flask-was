from flask import Flask
from flask_was import Was

app = Flask(__name__)
api = Was(app)
