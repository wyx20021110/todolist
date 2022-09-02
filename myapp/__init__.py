from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'wyx'

db = SQLAlchemy(app)
if True:

    from myapp import views
