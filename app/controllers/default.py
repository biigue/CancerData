from flask import render_template
from app import app

#Toda vez que criar um a página tem que adicionar a rota aqui
@app.route('/')
def Index():
    return render_template('index.html')