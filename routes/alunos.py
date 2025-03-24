from flask import Blueprint, render_template
from controler.cadastrarAluno import CadastrarAluno

cadastrar_alunos = Blueprint("cadastrar_alunos", __name__)

cadastrar_alunos.route('/alunos', method=["POST"])(CadastrarAluno.cadastrarAluno)