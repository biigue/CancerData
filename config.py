DEBUG = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bd_oncologia'
#localhost = hostname no mysql new connection
#ip,porta e ... p se conectar
"""app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:senha@server/connectioname'
db = SQLAlchemy(app)"""
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/bd_oncologia'
SQLALCHEMY_TRACK_MODIFICATIONS = True 