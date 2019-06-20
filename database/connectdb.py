from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
#ps.: na engine, com o echo = True você ativa o modo debug. 
 
class Connection:
 
    def session():
 
        connection_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
            "root", #"db_user"
            "", #db_pass
            "localhost", #db_host
            #"db_port", #db_port
            "bd_oncologia"  #db_name
        )
 
        # echo = True, ativa debug
        engine = create_engine(connection_string, echo=False)
        Session = sessionmaker(bind=engine)
 
        return Session()

    #funções abaixo q era de bianca antes, talvez tenha q apagar algo dessa classe pq ta repetindo, mas deixei aaq por enq
    def get_engine():
    
        user = "root"
        password = ""
        address = "localhost"
        database_name = "bd_oncologia"
        engine = create_engine('mysql+pymysql://%s:%s@%s/%s' % (user, password, address, database_name), echo=True)

        return engine


    def get_session():
        engine = get_engine()
        return sessionmaker(bind=engine)


    def init(drop_tables=False):
        engine = get_engine()
        if not database_exists(engine.url):
            create_database(engine.url)
        if drop_tables:
            Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        return sessionmaker(bind=engine)