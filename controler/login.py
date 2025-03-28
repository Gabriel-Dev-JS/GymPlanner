from flask import jsonify, redirect,request, url_for
from db import conexao
from repository import Repository

class Login:
    @staticmethod
    def login():
        try:
            conexao_bd = conexao('GymPlanner.db')
            repository = Repository(conexao_bd)
            data = request.get_json()

            if not data:
                return jsonify({"Error": "JSON invalido ou vazio"}), 400

            emailProfessor = data.get("email")
            senhaProfessor = data.get("senha")

            if not emailProfessor or not senhaProfessor:
                return jsonify({"Error": "Nome de usuário ou senha não fornecidos"}), 400
            
            professor = repository.findProfessor(email=emailProfessor, senha=senhaProfessor)
            if professor:
                return jsonify({"id":professor[0], "nome":professor[1]}), 201
            else:
                return jsonify({"Error": "credenciais invalidas"}), 401
        except Exception as e:
            return jsonify({"Error": str(e)}), 400