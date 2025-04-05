from flask import Blueprint, render_template, redirect, url_for
from controler.login import Login

login = Blueprint("login", __name__)

login.route('/login', methods=["POST"])(Login.login)
# @login.route('/', methods=["GET", "POST"])
# login.route('/login', methods=["GET", "POST"])
# def login_view():
#     return render_template('login.html')
    

