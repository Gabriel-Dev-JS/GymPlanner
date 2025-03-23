from flask import Blueprint, render_template

from controler.criarExercicio import ExercicioControler

exercicio_routes = Blueprint('exercicio_routes', __name__)

exercicio_routes.route('/aluno/<int:id_aluno>', methods=["POST"])(ExercicioControler.criarExercicio)
exercicio_routes.route('/aluno/<int:id_aluno>/<int:id_exercicio>', methods=["PUT"])(ExercicioControler.AtualizarExercicio)
exercicio_routes.route('/aluno/<int:id_aluno>/<int:id_exercicio>', methods=["DELETE"])(ExercicioControler.excluirExercicio)
exercicio_routes.route('/aluno/<int:id_aluno>', methods=["GET"])(ExercicioControler.listaExercicios)


@exercicio_routes.route('/criarExercicio', methods=["GET"])
def criarExercicioView():
    return render_template("cadastrarExercicio.html")