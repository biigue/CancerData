from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text, Date, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

#Ainda não testei
Base = declarative_base()

class Estado(Base):
    __tablename__ = "Estado"
    idEstado = Column("idEstado", Integer, primary_key=True, nullable=False)
    nome = Column("nome", Text)
    sigla = Column("sigla", Text, nullable=False)

class TipoDeExame(Base):
    __tablename__ = "TipoDeExame"
    idTipoDeExame = Column("idTipoDeExame", Integer, primary_key=True, nullable=False)
    tipoDeExame = Column("tipoDeExame", Text)
    
class Ano(Base):
    __tablename__ = "Ano"
    idAno = Column("idAno", Integer, primary_key=True, nullable=False)
    Ano = Column("Ano", Integer, nullable=True)

class Exame(Base):
    __tablename__ = "Exame"
    idExames = Column("idExames", Integer, primary_key=True, nullable=False)
    totalDeExames = Column("totalDeExames", Integer, nullable= False)
    tipoDeCancer = Column("tipoDeCancer", String(254), nullable= False)
    Estado_idEstado = Colum("Estado_idEstado", Integer, nullable= False, ForeignKey(Estado.idEstado))
    TipoDeExame_idTipoDeExame=  Colum("TipoDeExame_idTipoDeExame", Integer, nullable= False, ForeignKey(TipoDeExame.idTipoDeExame))
    Ano_idAno = Colum("Ano_idAno", Integer, nullable= False, ForeignKey(Ano.idAno))

class Mortalidade(Base):
    __tablename__ = "Mortalidade"
    idMortalidade = Column("idMortalidade", Integer, primary_key=True, nullable=False)
    numeroDeCasos = Column("numeroDeCasos", Integer, nullable= False)
    tipoDeCancer = Column("tipoDeCancer", String(254), nullable= False)
    raca = Column("raca", String(254), nullable= False)
    FaixaEtaria = Column("FaixaEtaria", String(254), nullable= False)
    Ano_idAno = Colum("Ano_idAno", Integer, nullable= False, ForeignKey(Ano.idAno))

class MamografosPorUF(Base):
    __tablename__ = "MamografosPorUF"
    idMamografosPorUF = Column("idMamografosPorUF", Integer, primary_key=True, nullable=False)
    quantidadeSUS = Column("quantidadeSUS", Integer, nullable= False)
    quantidadeNaoSUS = Column("quantidadeSUS", Integer, nullable= False)
    Estado_idEstado = Colum("Estado_idEstado", Integer, nullable= False, ForeignKey(Estado.idEstado))

class Cidade(Base):
    __tablename__ = "Cidade"
    idCidade = Column("idCidade", Integer, primary_key=True, nullable=False)
    nome = Column("nome", String(254), nullable= False)
    latitude = Column("latitude", String(254), nullable= False)
    longitude = Column("longitude", String(254), nullable= False)
    Estado_idEstado = Colum("Estado_idEstado", Integer, nullable= False, ForeignKey(Estado.idEstado))

class RazaoDeExames(Base):
    __tablename__ = "RazaoDeExames"
    idRazaoDeExames = Column("idRazaoDeExames", Integer, primary_key=True, nullable=False)
    nota = Column("longitude", Float, nullable= False)
    data = Column("data", String(254), nullable=False)
    TipoDeExame_idTipoDeExame=  Colum("TipoDeExame_idTipoDeExame", Integer, nullable= False, ForeignKey(TipoDeExame.idTipoDeExame))
    Cidade_idCidade = Colum("Cidade_idCidade", Integer, nullable= False, ForeignKey(Cidade.Cidade_idCidade))
    
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