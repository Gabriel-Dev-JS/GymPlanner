from flask import jsonify,request
from db import conexao
from repository import Repository

class CadastrarAluno:
    @staticmethod
    def cadastrarAluno(id_professor):
        try:
            conexao_bd = conexao('GymPlanner.db')
            repository = Repository(conexao_bd)
            data = request.get_json()
            
            nome = data.get('nome')
            sobrenome = data.get('sobrenome')
            email = data.get('email')
            senha = data.get('senha')


            professor = repository.findProfessorId(id_professor=id_professor)
            aluno = repository.findAluno(id_professor=id_professor, email=email)

            if not professor:
                return jsonify({"Erro": "Professor não encontrado"}), 400
            
            if aluno:
                return jsonify({"Erro": "Usuario já cadastrado"}), 401

            repository.createAluno(nome=nome, sobrenome=sobrenome, email=email, senha=senha, id_professor=id_professor)
            return jsonify({"nome":nome}), 201
        except Exception as e:
            return jsonify({"Error": str(e)}), 400