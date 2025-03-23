from flask import Blueprint
from controler.criarExercicio import ExercicioControler

exercicio_routes = Blueprint('exercicio_routes', __name__)

exercicio_routes.route('aluno/<int:id_aluno>', method=["POST"])(ExercicioControler.criarExercicio)
exercicio_routes.route('aluno/<int:id_aluno>/<int:id_exercicio>', method=["PUT"])(ExercicioControler.AtualizarExercicio)
exercicio_routes.route('aluno/<int:id_aluno>/<int:id_exercicio>', method=["DELETE"])(ExercicioControler.excluirExercicio)
exercicio_routes.route('aluno/<int:id_aluno>', method=["GET"])(ExercicioControler.listaExercicios)

# @exercicio_routes.route('/criarExercicio', methods=["POST"])
# def criarExercicio():
#     return ExercicioControler.criarExercicio()