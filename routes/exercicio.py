from flask import Blueprint, render_template, request

from controler.criarExercicio import ExercicioControler

exercicio_routes = Blueprint('exercicio_routes', __name__)

exercicio_routes.route('/aluno/<int:id_aluno>/<int:id_professor>', methods=["POST"])(ExercicioControler.criarExercicio)
exercicio_routes.route('/aluno/<int:id_aluno>/<int:id_exercicio>/<int:id_professor>', methods=["PUT"])(ExercicioControler.AtualizarExercicio)
exercicio_routes.route('/aluno/<int:id_aluno>/<int:id_exercicio>/<int:id_professor>', methods=["DELETE"])(ExercicioControler.excluirExercicio)
# exercicio_routes.route('/aluno/<int:id_aluno>/<int:id_professor>', methods=["GET"])(ExercicioControler.listarExercicios)

@exercicio_routes.route('/aluno/<int:id_professor>/<int:id_aluno>', methods=["GET"])
def alunos(id_professor, id_aluno):
    return render_template("aluno.html")

@exercicio_routes.route('/api/aluno/<int:id_professor>/<int:id_aluno>', methods=["GET"])
def alunos_api(id_professor, id_aluno):
    return ExercicioControler.listarExercicios(id_professor, id_aluno)

@exercicio_routes.route('/exercicio', methods=["GET"])
def criarExercicioView():
    return render_template("cadastrarExercicio.html")

@exercicio_routes.route('/login', methods=["GET"])
def loginView():
    return render_template("login.html")



