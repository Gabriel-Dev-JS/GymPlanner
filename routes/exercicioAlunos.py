from flask import Blueprint, render_template, request

from controler.criarExercicio import ExercicioControler

exercicio_alunos_routes = Blueprint('exercicio_alunos_routes', __name__)


@exercicio_alunos_routes.route('/exercicioAluno/<int:id_aluno>', methods=["GET"])
def alunos(id_aluno):
    return render_template("exercicioAlunos.html")

@exercicio_alunos_routes.route('/api/exercicioAluno/<int:id_aluno>', methods=["GET"])
def alunos_api(id_aluno):
    return ExercicioControler.listarExerciciosAluno(id_aluno)