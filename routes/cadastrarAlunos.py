from flask import Blueprint, render_template
from controler.cadastrarAluno import CadastrarAluno

listar_alunos = Blueprint("listar_alunos", __name__)

@listar_alunos.route('/cadastrar-aluno/<int:id_professor>', methods=["POST"])(CadastrarAluno.cadastrarAluno)
def modalCriarAlunoView():
    return render_template("cadastrarAluno.html")
