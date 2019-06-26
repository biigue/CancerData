import geopandas as gp
import pandas as pd
import matplotlib as mpl
import folium
from folium import plugins
import pymysql.cursors

def generateMap(tipo = "all"):

    connection = pymysql.connect(host="localhost", user="root", password="", db="bd_oncologia", cursorclass=pymysql.cursors.Cursor)

    if tipo == "all":
        query = "SELECT e.sigla, SUM(r.nota)/COUNT(*) FROM Estado as e JOIN Cidade as c JOIN RazaoDeExames as r ON r.Cidade_idCidade = c.idCidade AND c.Estado_idEstado = e.idEstado GROUP BY e.sigla;"
    else:
        query = "SELECT e.sigla, SUM(r.nota)/COUNT(*) FROM Estado as e JOIN Cidade as c JOIN RazaoDeExames as r JOIN TipoDeExame as t ON r.Cidade_idCidade = c.idCidade AND c.Estado_idEstado = e.idEstado AND r.TipoDeExame_idTipoDeExame = t.idTipoDeExame WHERE t.tipoDeExame = '{}' GROUP BY e.sigla;".format(tipo)

    infos = []
    with connection:
        cur = connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            infos.append([row[0], row[1]])

    df = pd.DataFrame(columns=["wikimedia", "nota"], data=infos, index=None)

    brazil = gp.read_file("app/analise/Central-West Region_AL3-AL4.shp")
    UF = ["AC", "AL", "AP", "AM", "BA", "CE", "ES", "DF", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

    for i in range(len(UF)):
        brazil["wikimedia"][i + 5] = UF[i]
        
    m = folium.Map(location=[-15.788497,-47.879873], zoom_start=4)

    folium.Choropleth(geo_data=brazil[5:], name="choropleth", line_opacity=0.2, data=df, columns=["wikimedia", "nota"], fill_color="YlGn", fill_opacity=1, legend_name="Nota", key_on="feature.properties.wikimedia").add_to(m)
    filename = "mapa-" + tipo + ".html"
    m.save("app/templates/" + filename)

    return True