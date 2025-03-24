from flask import jsonify,request
from repository import Repository

class CadastrarAluno:
    @staticmethod
    def cadastrarAluno(id_professor):
        try:
            data = request.get_json()
            nome = data.get('nome')
            sobrenome = data.get('sobrenome')

            repository = Repository()
            repository.createAluno(nome, sobrenome, id_professor)

            response = {
                "nome": nome,
                "sobrenome": sobrenome
            }

            return jsonify(response), 201
        except Exception as e:
            return jsonify({"Error": str(e)}), 400
        