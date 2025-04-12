from flask import Blueprint, render_template
from controler.cadastrarAluno import CadastrarAluno

cadastrar_alunos = Blueprint("cadastrar_alunos", __name__)

# cadastrar_alunos.route('/alunos/<int:id_professor>', methods=["POST"])(CadastrarAluno.cadastrarAluno)
cadastrar_alunos.route('/listarAlunos/<int:id_professor>', methods=["POST"])(CadastrarAluno.cadastrarAluno)
def modalCriarAlunoView():
    return render_template("cadastrarAluno.html")

# from flask import Blueprint, render_template, request
# from controler.cadastrarAluno import CadastrarAluno

# listar_alunos = Blueprint("listar_alunos", __name__)

# @listar_alunos.route('/cadastrar-aluno/<int:id_professor>', methods=["GET", "POST"])
# def modalCriarAlunoView(id_professor):
#     if request.method == "POST":
#         # Aqui, você chama o método do CadastrarAluno
#         CadastrarAluno.cadastrarAluno(id_professor)
#         # Adicione a lógica que for necessária após o POST, por exemplo, redirecionar para outra página
#     return render_template("cadastrarAluno.html")