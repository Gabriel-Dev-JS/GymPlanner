from flask import jsonify, redirect,request, url_for
from db import conexao
from repository import Repository

class Login:
    @staticmethod
    def login(user_type):
        try:
            conexao_bd = conexao('GymPlanner.db')
            repository = Repository(conexao_bd)
            data = request.get_json()

            if not data:
                return jsonify({"Error": "JSON invalido ou vazio"}), 400

            userEmail = data.get("email")
            userSenha = data.get("senha")

            professor = repository.findProfessor(email=userEmail, senha=userSenha)
            aluno = repository.findAlunoEmailSenha(email=userEmail, senha=userSenha)
            
               
            if user_type == 'aluno':
                if userEmail != aluno[3] and userSenha != aluno[4]:
                    return jsonify({"Error": "Nome de usuário ou senha não fornecidos"}), 400
            
            
            if user_type == 'professor':
                if userEmail != professor[3] and userSenha != professor[4]:
                    return jsonify({"Error": "Nome de usuário ou senha não fornecidos"}), 400

            if professor:
                return jsonify({"id":professor[0], "nome":professor[1]}), 201
            elif aluno:
                return jsonify({"id":aluno[0], "nome":aluno[1]}), 201
            else:
                return jsonify({"Error": "credenciais invalidas"}), 401
        except Exception as e:
            return jsonify({"Error": str(e)}), 400