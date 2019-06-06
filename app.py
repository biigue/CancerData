from flask import render_template
from flask import Flask
app = Flask(__name__) 


#Toda vez que criar um a página tem que adicionar a rota aqui
@app.route('/')
def Index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

