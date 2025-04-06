from flask import Blueprint, render_template, jsonify
from controler.listarAlunos import ListarAlunos

listar_alunos = Blueprint("listar_alunos", __name__)
controler = ListarAlunos()

@listar_alunos.route('/cadastrarAluno', methods=["GET"])
def modalCriarAlunoView():
    return render_template("cadastrarAluno.html")

@listar_alunos.route('/listarAlunos/<int:id_professor>', methods=["GET"])
def listarAlunoView(id_professor):
    return render_template("listarAluno.html")

@listar_alunos.route('/api/alunos/<int:id_professor>', methods=["GET"])
def listar_alunos_api(id_professor):
    return controler.listarAlunos(id_professor)  # Retorna o JSON
