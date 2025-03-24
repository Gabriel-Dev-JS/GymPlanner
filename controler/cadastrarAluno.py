from flask import jsonify,request
from repository import Repository

class CadastrarAluno:
    @staticmethod
    def cadastrarAluno():
        try:
            data = request.get_json()
            nome = data.get('nome')
            sobrenome = data.get('sobrenome')

            repository = Repository()
            repository.createAluno(nome, sobrenome)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
            