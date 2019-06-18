from flask import Flask, render_template
import pymysql
app = Flask(__name__)
class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = ""
        db = "bd_oncologia"
        port= "3306"
        
        self.con = pymysql.connect(host=host, port=port user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                    DictCursor)
        self.cur = self.con.cursor()

    def list_teste(self):
        self.cur.execute("SELECT * FROM estado LIMIT 50")
        result = self.cur.fetchall()
        return result

@app.route('/')
def employees():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('employees.html', result=res, content_type='application/json')

#Acho que não seria uma boa usar o conect mysql pq ceça teria q rodar o banco + rodar todos os scripts de insert(que demoram)
#Para só assim poder ter acesso no flask ( que a requisição feita pode demorar também ), mas se quiser fazer assim tem esse escopo