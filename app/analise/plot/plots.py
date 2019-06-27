import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

connection = Connection.session()

def gerar_grafico_mamografos_por_uf():
    return 0

def gerar_grafico_mamografos_distribuicao_por_regiao():
    return 0

def gerar_grafico_pizza_mamog_sus_e_nao_sus_brasil():
    return 0

def gerar_grafico_barras_exames_oncologia_por_estado():
    return 0 

def gerar_grafico_pizzas_exames_oncologia_por_regiao():
    return 0 

def gerar_grafico_barras(pathData):



def gerar_grafico_pizza(pathData):
    dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)

    hashtags = dataset[colunas[0]].values
    valores = dataset[colunas[1]].values

    dic = {'tags' : hashtags, 'val' : valores }

    df = pd.DataFrame(data=dic)
    df = df.sort_values('val')
    df['percent'] = (df['val'] / df['val'].sum()) * 100
    df['outros'] = df['percent'].cumsum()

    outros = df[df.percent <= 5]
    outros = outros.append({'tags': 'outros',
                             'percent': outros['percent'].sum()}, ignore_index=True)
    df = df[df.percent > 5]
    df = df[['tags', 'percent']]
    df = df.append({'tags': outros['tags'][len(outros['tags'])-1],
                     'percent': outros['percent'][len(outros['tags'])-1]}, ignore_index=True)
    df = df.sort_values('percent')

    hashtags = df['tags'].values
    valores = df['percent'].values

    labels = list(hashtags)
    vals = list(valores)

    cores = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    figura, ax = plt.subplots()
    ax.pie(vals, colors = cores, labels=labels, 
            autopct='%1.1f%%', startangle=90)

    centre_circle = plt.Circle((0,0),0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    ax.axis('equal')
    plt.tight_layout()
    plt.savefig('imagem-dois.png', bbox_inches='tight')
    
    plt.show()


