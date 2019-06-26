from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
#app.config.from_json("config.json")

app.config.from_object('config')
db = SQLAlchemy(app)

#migrate cuida das migrações
migrate = Migrate(app,db)
migrate = Migrate(app,db)

#manager  cuida dos comandos para inicializar a nossa aplicação. ex: runserver
manager = Manager(app)
manager.add_command('db',MigrateCommand)

from app.controllers import default
