from flask import Blueprint, render_template

from controler.criarExercicio import ExercicioControler

exercicio_routes = Blueprint('exercicio_routes', __name__)

#rotas de CRUD exercicio
exercicio_routes.route('/aluno/<int:id_aluno>', methods=["POST"])(ExercicioControler.criarExercicio)
exercicio_routes.route('/aluno/<int:id_aluno>/<int:id_exercicio>', methods=["PUT"])(ExercicioControler.AtualizarExercicio)
exercicio_routes.route('/aluno/<int:id_aluno>/<int:id_exercicio>', methods=["DELETE"])(ExercicioControler.excluirExercicio)
exercicio_routes.route('/aluno/<int:id_aluno>', methods=["GET"])(ExercicioControler.listaExercicios)


#rota view cadastro exercicio
@exercicio_routes.route('/exercicio', methods=["GET"])
def criarExercicioView():
    return render_template("cadastrarExercicio.html")

#rota view login
@exercicio_routes.route('/login', methods=["GET"])
def loginView():
    return render_template("login.html")

#rota view listar Alunos
@exercicio_routes.route('/listaAlunos', methods=["GET"])
def listarAlunoView():
    return render_template("listarAluno.html")

