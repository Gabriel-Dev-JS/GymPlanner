from flask import jsonify,request
from db import conexao
from repository import Repository

class ExercicioControler:
    @staticmethod
    def criarExercicio(id_aluno, id_professor):
        try:

            conexao_bd = conexao('GymPlanner.db')
            repository = Repository(conexao_bd)
            data = request.get_json()
            
            if not data:
                return jsonify({"error": "JSON inválido ou vazio"}), 400
            
            exercicio = data.get('exercicio')
            repeticao = data.get('repeticao')
            serie = data.get('serie')

            professor = repository.findProfessorId(id_professor=id_professor)

            if not professor:
                return jsonify({"Error": "Professor não encontrado"}), 400
            
            repository.createExercicio(exercicio=exercicio, repeticao=repeticao, serie=serie, id_aluno=id_aluno, id_professor=id_professor)

            response = {
                "message": "Exercicio criado com sucesso",
                "exercicio": exercicio,
                "repeticao": repeticao,
                "serie": serie
            }
            return jsonify(response), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400


    @staticmethod
    def excluirExercicio(id_exercicio,id_aluno, id_professor):
        try:
            conexao_bd = conexao('GymPlanner.db')
            repository = Repository(conexao_bd)
            repository.removeExercicio(id_exercicio=id_exercicio, id_aluno=id_aluno, id_professor=id_professor)

            response = {
                "message": "Exercicio excluido com sucesso"
            }

            return jsonify(response), 201
        except Exception as e:
            return jsonify({"error":str(e)}), 400 
        
    @staticmethod    
    def AtualizarExercicio(id_exercicio, id_aluno, id_professor):
        try:

            data = request.get_json()

            if not data:
                return jsonify({"error": "JSON inválido ou vazio"}), 400

            exercicio = data.get('exercicio')
            repeticao = data.get('repeticao')
            serie = data.get('serie')

            conexao_bd = conexao('GymPlanner.db')
            repository = Repository(conexao_bd)
            repository.updateExercio(exercicio=exercicio, repeticao=repeticao, serie=serie, id_exercicio=id_exercicio, id_aluno=id_aluno, id_professor=id_professor)

            response = {
                "message": "exercicio atualizado com sucesso",
                "exercicio": exercicio,
                "repeticao": repeticao,
                "serie": serie
            }

            return jsonify(response), 201
        
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @staticmethod    
    def listarExercicios(id_aluno, id_professor):
        try:
            conexao_bd = conexao('GymPlanner.db')
            repository = Repository(conexao_bd)
            response = repository.findAllExercicio(id_aluno=id_aluno,id_professor=id_professor)
            return jsonify({"exercicio":response}), 201
            # return jsonify({"exercicio":"response"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 401
        