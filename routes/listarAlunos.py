from flask import Blueprint, render_template
from controler.listarAlunos import ListarAlunos

listar_alunos = Blueprint("listar_alunos", __name__)

listar_alunos.route('/alunos/<int:id_professor>', methods=["GET"])(ListarAlunos.listarAlunos)

@listar_alunos.route('/alunos/<int:id_professor>', methods=["GET"])
def modalCriarAlunoView():
    return render_template("listarExercicio.html")
