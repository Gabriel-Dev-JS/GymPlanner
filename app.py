from flask import Flask 

app = Flask(__name__)
# teste
@app.route('/')
def index():
    error = "não foi possivel concluir esta operação"
    try:
        # d = 4/2
        d = 1/0
        return f"Resultado: {d}"
    except:
        return f"Erro: {error}" 
    

if __name__ == "__main__":
    app.run(debug=True) 
