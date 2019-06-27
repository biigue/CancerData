from flask import render_template, redirect, url_for
from app import app #, db

#Toda vez que criar um a página tem que adicionar a rota aqui
@app.route('/')
def Index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found():
    return render_template('404.html'),404

@app.route('/mamografos')
def mamografos():
    return render_template('mamografos.html')

@app.route('/distribuicaoexames')
def distribuicaoExames():
    return render_template('distribuicaoexames.html')

@app.route('/mortalidade')
def mortalidade():
    return render_template('mortalidade.html')

@app.route('/tiposexames')
def tiposExames():
    return render_template('tiposexames.html')

@app.route('/choropleth')
def mapaDeCalor1():
    return render_template('mapadecalor1.html')

@app.route('/mapadecalor2')
def mapaDeCalor2():
    return render_template('mapadecalor2.html')

@app.route('/criadores')
def criadores():
    return render_template('criadores.html')

@app.route("/choroplethgeral")
def choroplethGeral():
    return render_template("mapa-all.html")

@app.route("/choroplethcolodeutero")
def choroplethColoDeUtero():
    return render_template("mapa-citopatologico.html")

@app.route("/choroplethmamografia")
def choroplethMamografia():
    return render_template("mapa-mamografia.html")