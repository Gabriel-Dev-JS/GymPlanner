from flask import jsonify, redirect,request, url_for
from repository import Repository

class Login:
    @staticmethod
    def login():
        try:
            data = request.get_json()

            if not data:
                return jsonify({"Error": "JSON invalido ou vazio"}), 400

            nomeProfessor = data.get("email")
            senhaProfessor = data.get("senha")

            if not nomeProfessor or not senhaProfessor:
                return jsonify({"Error": "Nome de usuário ou senha não fornecidos"}), 400
            
            repository = Repository()
            professor = repository.findProfessor(nome=nomeProfessor, senha=senhaProfessor)

            if professor:
                return jsonify({"nome":professor.nome ,"id":professor.id}), 201
            else:
                return jsonify({"Error": "credenciais invalidas"}), 401
        except Exception as e:
            return jsonify({"Error": str(e)}), 400