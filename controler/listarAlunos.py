from flask import jsonify, request
from db import conexao
from repository import Repository

class ListarAlunos:
    @staticmethod
    def listarAlunos(id_professor): 
        conexao_bd = conexao('GymPlanner.db')
        repository = Repository(conexao_bd)

        try:
            professor = repository.findAllAluno(id_professor=id_professor)

            if not professor:
                return jsonify({"Error": "Professor não encontrado"}), 401
            
            alunos = repository.findAllAluno(id_professor=id_professor)
            
            return jsonify(alunos)
        
        except Exception as e:
            return jsonify({"Error":str(e)}), 400