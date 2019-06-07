from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_json("config.json")
#localhost = hostname no mysql new connection
"""app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:senha@localhost/connectioname'
db = SQLAlchemy(app)"""

from app.controllers import default
