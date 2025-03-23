from flask import jsonify,request,Response
from repository import Repository

class ExercicioControler:
    @staticmethod
    def criarExercicio():
        try:
            data = request.get_json()
            
            if not data:
                return jsonify({"error": "JSON inválido ou vazio"}), 400
            
            exercicio = data.get('exercicio')
            repeticao = data.get('repeticao')
            serie = data.get('serie')
            id_aluno = data.get('id_aluno')

            repository = Repository()
            repository.createExercicio(exercicio, repeticao, serie, id_aluno)

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
    def excluirExercicio(id_exercicio):
        try:
            repository = Repository()
            repository.removeExercicio(id_exercicio)

            response = {
                "message": "Exercicio excluido com sucesso"
            }

            return jsonify(response), 201
        except Exception as e:
            return jsonify({"error":str(e)}), 400 
        
    @staticmethod    
    def AtualizarExercicio(id_exercicio):
        try:

            data = request.get_json()

            if not data:
                return jsonify({"error": "JSON inválido ou vazio"}), 400

            exercicio = data.get('exercicio')
            repeticao = data.get('repeticao')
            serie = data.get('serie')

            repository = Repository()
            repository.updateExercio(exercicio, repeticao, serie, id_exercicio)

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
    def listaExercicios(id_aluno):
        try:
            repository = Repository()
            repository.findAllExercicio(id_aluno)


        except Exception as e:
            return jsonify({"error": str(e)}), 401
        