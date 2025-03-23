from flask import Blueprint, render_template
from controler.login import Login

listar_alunos = Blueprint("listar_alunos", __name__)

listar_alunos.route('/listar-alunos', methods=["POST"])(Login.login)

@listar_alunos.route('/cadastrarAluno', methods=["GET"])
def modalCriarAlunoView():
    return render_template("cadastrarAluno.html")
