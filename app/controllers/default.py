from flask import render_template
from app import app

#Toda vez que criar um a página tem que adicionar a rota aqui
@app.route('/')
def Index():
    return render_template('index.html')

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

@app.route('/mapadecalor1')
def mapaDeCalor1():
    return render_template('mapadecalor1.html')

@app.route('/mapadecalor2')
def mapaDeCalor2():
    return render_template('mapadecalor2.html')

@app.route('/criadores')
def criadores():
    return render_template('criadores.html')