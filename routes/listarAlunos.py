from flask import Blueprint
from controler.login import Login

listar_alunos = Blueprint("listar_alunos", __name__)

listar_alunos.route('/listar-alunos', method=["Post"])(Login.login)