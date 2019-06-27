import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
import pymysql

host = "localhost"
user = "root"
password = "root"
db = "bd_oncologia"
port = 3306

con = pymysql.connect(host, user, password, db, port, autocommit=True)

cur = con.cursor()
cur.execute(
        "select a.quantidadeSUS, a.quantidadeNaoSUS, b.sigla from MamografosPorUF as a inner join Estado as b where a.Estado_idEstado = b.idEstado;")

def gerar_grafico_com_lista():
    sus = []
    nsus = []
    sigla = []
    rows = cur.fetchall()

    for row in rows:
        susString = format(row[0])
        nsusString = format(row[1])
        siglaString = format(row[2])
        sus.append(int(susString))
        nsus.append(int(nsusString))
        sigla.append(siglaString)

    return sus, nsus, sigla



def gerar_grafico_mamografos_total_regiao(pathData):
    """dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)
    sus=dataset[colunas[0]].values.tolist()
    nsus=dataset[colunas[1]].values.tolist()
    siglas = dataset[colunas[2]].values.tolist()
    #regiao=dataset[colunas[3]].values.tolist()"""
    sus, nsus, siglas = gerar_grafico_com_lista()

    #fazer lista com regiao de acordo com sigla
    regioes = ["norte", "nordeste", "centro-oeste", "sudeste", "sul"]
    regiao = []
    divisao = [
        ['AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC'],
        ['MA', 'PI', 'CE', 'RN', 'PE', 'PB', 'SE', 'AL', 'BA'],
        ['MT', 'MS', 'GO', 'DF'],
        ['SP', 'RJ', 'ES', 'MG'],
        ['PR', 'RS', 'SC']
    ]
    for i in range(len(siglas)):
        for j in range(len(divisao)):
            if (siglas[i] in divisao[j]):
                regiao.append(regioes[j])
    valor_sus_reg=[]
    norte=0
    nordeste=0
    sudeste=0
    sul=0
    centro=0
    cont=0
    for i in regiao:
        if i=='norte':
            norte+=sus[cont]
            norte += nsus[cont]
        if i=='nordeste':
            nordeste+=sus[cont]
            nordeste += nsus[cont]
        if i=='sudeste':
            sudeste+=sus[cont]
            sudeste += nsus[cont]
        if i=='sul':
            sul+=sus[cont]
            sul += nsus[cont]
        if i=='centro-oeste':
            centro+=sus[cont]
            centro += nsus[cont]
        cont += 1
    valor_sus_reg.append(norte)
    valor_sus_reg.append(nordeste)
    valor_sus_reg.append(sudeste)
    valor_sus_reg.append(sul)
    valor_sus_reg.append(centro)

    regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

    pyplot.axis('equal')
    pyplot.pie(valor_sus_reg, labels=regioes, autopct='%1.1f%%')

    pyplot.title('Distribuição do total de mamógrafos por regiões do Brasil')
    pyplot.savefig('graficos\mamografos-total-regiao.png')

def gerar_grafico_mamografos_sus_regiao(pathData):
    """dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)
    sus=dataset[colunas[0]].values.tolist()
    nsus=dataset[colunas[1]].values.tolist()
    #regiao=dataset[colunas[3]].values.tolist()
    siglas = dataset[colunas[2]].values.tolist()"""
    sus, nsus, siglas = gerar_grafico_com_lista()

    regioes = ["norte", "nordeste", "centro-oeste", "sudeste", "sul"]

    regiao = []

    divisao = [
        ['AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC'],
        ['MA', 'PI', 'CE', 'RN', 'PE', 'PB', 'SE', 'AL', 'BA'],
        ['MT', 'MS', 'GO', 'DF'],
        ['SP', 'RJ', 'ES', 'MG'],
        ['PR', 'RS', 'SC']
    ]

    for i in range(len(siglas)):
        for j in range(len(divisao)):
            if (siglas[i] in divisao[j]):
                regiao.append(regioes[j])

    valor_sus_reg=[]
    norte=0
    nordeste=0
    sudeste=0
    sul=0
    centro=0
    cont=0
    for i in regiao:
        if i=='norte':
            norte+=sus[cont]
        if i=='nordeste':
            nordeste+=sus[cont]
        if i=='sudeste':
            sudeste+=sus[cont]
        if i=='sul':
            sul+=sus[cont]
        if i=='centro-oeste':
            centro+=sus[cont]
        cont += 1
    valor_sus_reg.append(norte)
    valor_sus_reg.append(nordeste)
    valor_sus_reg.append(sudeste)
    valor_sus_reg.append(sul)
    valor_sus_reg.append(centro)

    regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

    pyplot.axis('equal')
    pyplot.pie(valor_sus_reg, labels=regioes, autopct='%1.1f%%')

    pyplot.title('Distribuição do total de mamógrafos do sus por regiões do Brasil')
    pyplot.savefig('graficos\mamografos-total-sus-regiao.png')

def gerar_grafico_mamografos_nsus_regiao(pathData):
    """dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)
    sus=dataset[colunas[0]].values.tolist()
    nsus=dataset[colunas[1]].values.tolist()

    siglas = dataset[colunas[2]].values.tolist()"""
    sus, nsus, siglas = gerar_grafico_com_lista()

    regioes = ["norte", "nordeste", "centro-oeste", "sudeste", "sul"]

    regiao = []

    divisao = [
        ['AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC'],
        ['MA', 'PI', 'CE', 'RN', 'PE', 'PB', 'SE', 'AL', 'BA'],
        ['MT', 'MS', 'GO', 'DF'],
        ['SP', 'RJ', 'ES', 'MG'],
        ['PR', 'RS', 'SC']
    ]

    for i in range(len(siglas)):
        for j in range(len(divisao)):
            if (siglas[i] in divisao[j]):
                regiao.append(regioes[j])

    valor_sus_reg=[]
    norte=0
    nordeste=0
    sudeste=0
    sul=0
    centro=0
    cont=0
    for i in regiao:
        if i=='norte':
            norte += nsus[cont]
        if i=='nordeste':
            nordeste += nsus[cont]
        if i=='sudeste':
            sudeste += nsus[cont]
        if i=='sul':
            sul += nsus[cont]
        if i=='centro-oeste':
            centro += nsus[cont]
        cont += 1
    valor_sus_reg.append(norte)
    valor_sus_reg.append(nordeste)
    valor_sus_reg.append(sudeste)
    valor_sus_reg.append(sul)
    valor_sus_reg.append(centro)

    regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

    pyplot.axis('equal')
    pyplot.pie(valor_sus_reg, labels=regioes, autopct='%1.1f%%')

    pyplot.title('Distribuição do total de mamógrafos privados por regiões do Brasil')
    pyplot.savefig('graficos\mamografos-nsus-regiao.png')

def gerar_grafico_mamografos_razao_sus_nsus(pathData):
    """dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)
    sus=sum(dataset[colunas[0]].values.tolist())
    nsus=sum(dataset[colunas[1]].values.tolist())"""
    sus, nsus, siglas = gerar_grafico_com_lista()
    valores=[]
    valores.append(sum(sus))
    valores.append(sum(nsus))

    pyplot.axis('equal')
    pyplot.pie(valores, labels=['SUS','Rede Privada'], autopct='%1.1f%%')

    pyplot.title('Distribuição dos mamográfos em relação ao SUS e Rede Privada no Brasil')
    pyplot.savefig('graficos\mamografos-razao-sus-nsus.png')

def gerar_grafico_mamografos_por_estado(pathData):
    """dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)
    sus=dataset[colunas[0]].values.tolist()
    nsus=dataset[colunas[1]].values.tolist()
    sigla=dataset[colunas[2]].values.tolist()"""
    sus, nsus, sigla = gerar_grafico_com_lista()
    for i  in range(len(sigla)):
        valores=[]
        valores.append(sus[i])
        valores.append(nsus[i])
        pyplot.axis('equal')
        pyplot.pie(valores, labels=['SUS', 'Rede Privada'], autopct='%1.1f%%')

        pyplot.title(sigla[i])
        pyplot.savefig(sigla[i]+'.png')

def gerar_grafico_mamografos_barra_todos_estados(pathData):
    dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)
    sus=dataset[colunas[0]].values.tolist()
    nsus=dataset[colunas[1]].values.tolist()
    sigla=dataset[colunas[2]].values.tolist()
    total=[]
    for i in range(len(sigla)):
        tot= sus+nsus
        total.append(tot)

    hashtags = dataset[colunas[0]].values
    valores = dataset[colunas[1]].values

    dic = {'Estados': sigla, 'Numero de Mamografos': valores}

    df = pd.DataFrame(data=dic)
    df = df.sort_values('Numero de Mamografos', ascending=False)
    df.set_index('Estados', inplace=True)

    ax = df.plot.bar(y='Numero de Mamografos', legend=False)
    ax.set_ylabel('quantidade absoluta')
    ax.set_xlabel('Sigla dos Estados')

    pyplot.title('Quantidade de Mamografos por estado')
    pyplot.xticks(np.arange(0, len(hashtags), step=1), rotation=30)
    pyplot.subplots_adjust(top=0.926, bottom=0.195, left=0.074, right=0.981, hspace=0.2, wspace=0.2)
    pyplot.savefig('graficos\mamografos-barra-estado.png', bbox_inches='tight')

gerar_grafico_mamografos_total_regiao(r'')
gerar_grafico_mamografos_sus_regiao(r'')
gerar_grafico_mamografos_nsus_regiao(r'')
gerar_grafico_mamografos_razao_sus_nsus(r'')
gerar_grafico_mamografos_por_estado(r'')
gerar_grafico_mamografos_barra_todos_estados(r'/home/djairb/Área de Trabalho/pasta-bianca/atv_bianca/mamo.csv')
