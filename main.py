from flask import Flask 
from routes.exercicio import exercicio_routes
from routes.listarAlunos import listar_alunos
from routes.alunos import cadastrar_alunos

app = Flask(__name__)

app.register_blueprint(exercicio_routes)
app.register_blueprint(listar_alunos)
app.register_blueprint(cadastrar_alunos)


if __name__ == "__main__":
    app.run(debug=True) 
