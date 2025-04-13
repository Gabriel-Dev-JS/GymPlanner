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

            response = list(map(lambda i: {
                "id":i[0],
                "nome":i[1],
                "sobrenome":i[2]
            }, alunos))
                
            return jsonify(response)
        
        except Exception as e:
            return jsonify({"Error":str(e)}), 400
        
    @staticmethod
    def excluirAluno(id_professor):
        conexao_bd = conexao('GymPlanner.db')
        repository = Repository(conexao_bd)
        
        try:
            data = request.get_json()
            id_aluno = data.get('id_aluno')
            repository.removeAluno(id_professor=id_professor, id_aluno=id_aluno)
            return jsonify({"Aluno deletado": id_aluno}), 201
        except Exception as e:
            return jsonify({"Error": str(e)}), 400

        
