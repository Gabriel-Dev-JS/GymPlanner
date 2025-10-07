from flask import Blueprint, render_template
from controler.login import Login

login = Blueprint("login", __name__)

@login.route('/login/<string:user_type>', methods=["POST"])
def loginRoute(user_type):
    if user_type not in ['professor', 'aluno']:
        return {'error':'Nada foi encontrado'}, 400
    return Login.login(user_type)

@login.route('/login', methods=["GET"]) 
def loginView():
    return render_template("login.html")