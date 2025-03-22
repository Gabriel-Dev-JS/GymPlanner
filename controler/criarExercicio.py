from flask import jsonify,request,Response
from repository import Repository

class ExercicioControler:
    @staticmethod
    def criarExercicio():
        try:
            data = request.get_json()
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

        