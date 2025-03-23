from flask import Flask 
from routes.exercicio import exercicio_routes

app = Flask(__name__)


app.register_blueprint(exercicio_routes)


if __name__ == "__main__":
    app.run(debug=True) 
