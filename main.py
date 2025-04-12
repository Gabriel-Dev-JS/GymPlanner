from flask import Flask, redirect, url_for 
from repository import Repository
from routes.exercicio import exercicio_routes
from routes.listarAlunos import listar_alunos
from routes.cadastrarAlunos import cadastrar_alunos
from routes.login import login
from db import conexao

app = Flask(__name__)

conexao_bd = conexao('GymPlanner.db') 
repository = Repository(conexao_bd)

app.register_blueprint(exercicio_routes)
app.register_blueprint(listar_alunos)
app.register_blueprint(cadastrar_alunos)
app.register_blueprint(login)


@app.route('/')
def home():
    return redirect(url_for('login.login'))

if __name__ == "__main__":
    app.run(debug=True) 
