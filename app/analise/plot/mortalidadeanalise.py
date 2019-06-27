import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from app import db
from pandas import DataFrame
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from sqlalchemy import create_engine
#import MySQLdb as mysql
import sys

engine = create_engine('mysql+pymysql://root:@localhost:3306/bd_oncologia')
#engine = create_engine('mysql//root:@localhost/bd_oncologia')

#engine = db.create_engine('dialect+driver://user:pass@host:port/db')
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/bd_oncologia'
conn = engine.connect()

engine = db.create_engine('mysql+pymysql://root:@localhost:3306/bd_oncologia')
connection = engine.connect()


def gerar_grafico_mortalidade_todos_tipos_cancer_total(engine):
    #result = pd.read_sql_query("SELECT tipoDeCancer,count(*)tipoDeCancer FROM mortalidade GROUP BY tipoDeCancer ;", engine)
    result = pd.read_sql_query("SELECT tipoDeCancer,numeroDeCasos FROM mortalidade GROUP BY tipoDeCancer  ;", engine , index_col=["tipoDeCancer"])
    my_df = pd.DataFrame.from_dict(result)
    my_df = my_df.sort_values('tipoDeCancer', ascending=False).head(6)
    plt.ylabel("Numero de mortes")
    plt.xlabel("Tipo de câncer")
    my_df.plot(kind='bar' ,title="mortalidades por tipo de cancer de todos os anos disponiveis(2000 a 2015) e de todas as faixas etárias",figsize=(6, 5))

    plt.savefig("../../static/imagens/mortalidade/mortalidadeportiposdecancerall.png", bbox_inches='tight')

def mortalidade_tipocancer_todasdatas_todas_faixasetarias(tipoCancer,engine):
    result = pd.read_sql_query("SELECT tipoDeCancer,numeroDeCasos,raca FROM mortalidade GROUP BY raca ;", engine)
    my_df = pd.DataFrame.from_dict(result)
    my_df.head()
    my_df.plot()
    plt.title("mortalidades pelo tipo de cancer X de todos os anos disponiveis(2000 a 2015) e por faixas etárias")
    plt.ylabel("Numero de mortes")
    plt.xlabel("Faixa etária")
    plt.savefig("../../static/imagens/mortalidade/mortalidadetipocancerescolhidoalldatasefaixas.png", bbox_inches='tight')
    result.plot()
    plt.show()
    

def mortalidade_tipocancer_intervalodata_todas_faixasetarias(tipoCancer,inicioAno,fimAno,engine):
    result = pd.read_sql_query("SELECT tipoDeCancer,numeroDeCasos,raca FROM mortalidade GROUP BY raca ;", engine , index_col=["FaixaEtaria"])
    my_df = pd.DataFrame.from_dict(result)
    plt.title("mortalidades por tipo de cancer X do ano YS a YX e de todas as faixas etárias")
    plt.ylabel("Numero de mortes")
    plt.xlabel("Tipo de câncer")

    plt.savefig("../../static/imagens/mortalidade/mortalidadeporcancerescolhidointervaloescolhidoporfaixaetaria.png", bbox_inches='tight')
    ax.savefig("matplotlib_legends2.png")
    result.plot()
    plt.show()

def mortos_pelo_tipo_escolhido_cancer_racas_diferentes_intervalo_anos(tipoCancer,inicioAno,fimAno,engine):
    result = pd.read_sql_query("SELECT tipoDeCancer,numeroDeCasos,raca FROM mortalidade GROUP BY raca ;", engine , index_col=["raca"])
    my_df = pd.DataFrame.from_dict(result)
    my_df.head()
    my_df.plot()
    plt.title("mortalidades por tipo de cancer X por raça e dentro do intervalo de X anos e Y anos ")
    plt.ylabel("Numero de mortes")
    plt.xlabel("Raça")
    #plt.kind("bar")
    #plt.style.use(['default'])
    #x_axis = my_df()
    #plt.style.use('classic')
    #plt.style.use('ggplot')
    #plt.style.use('fivethirtyeight')
    #plt.bar.color=""
    #plt.bar(x_axis,y_axis)

    plt.savefig("../../static/imagens/mortalidade/mortalidadeporcancerescolhidoracaeintervaloescolhido.png", bbox_inches='tight')
    result.plot()
    plt.show()



gerar_grafico_mortalidade_todos_tipos_cancer_total(engine)


