from flask import Blueprint
from controler.criarExercicio import ExercicioControler

exercicio_routes = Blueprint('exercicio_routes', __name__)

# exercicio_routes.route('/criarExercicio', method=["POST"])(ExercicioControler.criarExercicio)

# @exercicio_routes.route('/criarExercicio', methods=["POST"])
# def criarExercicio():
#     return ExercicioControler.criarExercicio()