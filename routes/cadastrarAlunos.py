from flask import Blueprint, render_template
from controler.cadastrarAluno import CadastrarAluno

cadastrar_alunos = Blueprint("cadastrar_alunos", __name__)

cadastrar_alunos.route('/listarAlunos/<int:id_professor>', methods=["POST"])(CadastrarAluno.cadastrarAluno)
def modalCriarAlunoView():
    return render_template("cadastrarAluno.html")