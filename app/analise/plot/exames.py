import numpy as np
import matplotlib.pyplot as pyplot
import pymysql

host = "localhost"
user = "root"
password = "root"
db = "bd_oncologia"
port = 3306

con = pymysql.connect(host, user, password, db, port, autocommit=True)

cur = con.cursor()

def grafico_barra_qtd_exames_realizados():
    cur.execute(
        "SELECT t.tipoDeExame, sum(e.totalDeExames) as numeroDeCasos FROM TipoDeExame as t JOIN Exames as e on t.idTipoDeExame = e.TipoDeExame_idTipoDeExame GROUP BY t.idTipoDeExame")

    rows = cur.fetchall()

    exames = []
    valores = []

    for row in rows:
        tipoDeExame = format(row[0])
        valorDoExame = format(row[1])
        exames.append(tipoDeExame[0].upper() + tipoDeExame[1::])

        valores.append(int(valorDoExame))

    y_pos = np.arange(len(exames))

    pyplot.bar(y_pos, valores, align='center', alpha=0.5)
    pyplot.xticks(y_pos, exames)
    pyplot.ylabel('Quantidade de Exames')
    pyplot.xlabel('Tipo de Exames')
    pyplot.title('Tipos de Exames Realizados no País')
    pyplot.savefig('graficos\exames_grafico_barra_qtd_exames_realizados.png')
    #plt.show()



def preencher_listas_exames(sigla, totalExame):
    cur.execute(
        "select es.sigla, ti.tipoDeExame, sum(ex.totalDeExames) from bd_oncologia.Exames as ex join bd_oncologia.Estado as es join bd_oncologia.TipoDeExame as ti on ex.Estado_idEstado = es.idEstado and ex.TipoDeExame_idTipoDeExame = ti.idTipoDeExame group by es.sigla, ti.tipoDeExame;")

    rows = cur.fetchall()

    sigla = []
    totalExame = []
    for row in rows:
        siglaAdd = format(row[0])
        valorExame = format(row[2])
        sigla.append(siglaAdd)
        totalExame.append(int(valorExame))
    return sigla, totalExame


def grafico_barra_qtd_exames_por_estado():
    sigla = []
    totalExame = []
    sigla, totalExame = preencher_listas_exames(sigla, totalExame)

    siglaMain = []
    for i in sigla:
        if (i not in siglaMain):
            siglaMain.append(i)

    citopatologico = []
    mamografia = []
    add = 1
    for i in totalExame:
        if (add):
            citopatologico.append(i)
            add = 0
        else:
            add = 1
    for j in totalExame:
        if j not in citopatologico:
            mamografia.append(j)

    N = 27
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = pyplot.figure()
    ax = fig.add_subplot(111)

    rects1 = ax.bar(ind, citopatologico, width, color='r')

    rects2 = ax.bar(ind + width, mamografia, width, color='g')

    ax.set_ylabel('Scores')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(tuple(siglaMain))
    ax.legend((rects1[0], rects2[0]), ('Citopatologico', 'Mamografia'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    #pyplot.show()
    pyplot.savefig('graficos\exames_grafico_barra_qtd_exames_por_estado.png')

def grafico_pizza_oncologia_por_regiao():
    sigla = []
    totalExame = []
    sigla, totalExame = preencher_listas_exames(sigla, totalExame)

    estados = []
    for i in sigla:
        if (i not in estados):
            estados.append(i)

    citopatologia = []
    mamografia = []
    add = 1
    for i in totalExame:
        if (add):
            citopatologia.append(i)
            add = 0
        else:
            add = 1
    for j in totalExame:
        if j not in citopatologia:
            mamografia.append(j)

    valorPorEstado = []

    for i in range(len(estados)):
        valor1 = citopatologia[i]
        valor2 = mamografia[i]
        soma = valor1 + valor2
        valorPorEstado.append(soma)

    regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

    divisao = [
        ['AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC'],
        ['MA', 'PI', 'CE', 'RN', 'PE', 'PB', 'SE', 'AL', 'BA'],
        ['MT', 'MS', 'GO'],
        ['SP', 'RJ', 'ES', 'MG'],
        ['PR', 'RS', 'SC']
    ]

    valoresPorRegiao = []

    for i in range(len(regioes)):
        valorProBanco = 0
        for j in range(len(estados)):
            ac = estados[j]
            if (estados[j] in divisao[i]):
                valorProBanco += valorPorEstado[j]
        valoresPorRegiao.append(valorProBanco)

    pyplot.axis('equal')
    pyplot.pie(valoresPorRegiao, labels=regioes, autopct='%1.1f%%')

    pyplot.title('Distribuição do total de exames relacionados à oncologia realizados por região do Brasil')
    #pyplot.show()
    pyplot.savefig('graficos\exames_grafico_pizza_oncologia_por_regiao.png')

grafico_barra_qtd_exames_por_estado()
grafico_barra_qtd_exames_realizados()
grafico_pizza_oncologia_por_regiao()