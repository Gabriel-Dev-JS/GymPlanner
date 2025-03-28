from flask import Blueprint, render_template
from controler.cadastrarAluno import CadastrarAluno

cadastrar_alunos = Blueprint("cadastrar_alunos", __name__)
# cadastrar_alunos.route('/alunos/<int:id_professor>', methods=["POST"])(CadastrarAluno.cadastrarAluno)
cadastrar_alunos.route('/listar-alunos/<int:id_professor>', methods=["POST"])(CadastrarAluno.cadastrarAluno)