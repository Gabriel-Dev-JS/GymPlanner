from flask import Blueprint, render_template
from controler.login import Login

login = Blueprint("login", __name__)

login.route('/login', methods=["POST"])(Login.login)

@login.route('/login', methods=["GET"])
def loginView():
    return render_template("login.html")