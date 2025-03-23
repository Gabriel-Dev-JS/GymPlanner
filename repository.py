from db import conexao

class Repository:
    def __init__(self, conexao: conexao):
        self.conexao = conexao
        self.cursor = self.conexao.get_cursor()
        self.createTableProfessor()
        self.createTableAluno()
        self.createTableExercicio()

    def createTableProfessor(self):
        query = """CREATE TABLE IF NOT EXISTS professor (
        id_professor INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
        nome TEXT,
        sobrenome TEXT,
        email TEXT,
        senha TEXT
        )"""

        self.cursor.execute(query)
        self.conexao.commit()
       


    def createTableAluno(self):
        query = """CREATE TABLE IF NOT EXISTS aluno (
        id_aluno INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
        nome TEXT,
        sobrenome TEXT,
        id_professor INTEGER,
        FOREIGN KEY (id_professor) REFERENCES professor (id_professor)
        )"""

        self.cursor.execute(query)
        self.conexao.commit()
    
    def createTableExercicio(self):
        query = """CREATE TABLE IF NOT EXISTS exercicio (
        id_exercicio INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
        exercicio TEXT,
        repeticao INTEGER,
        serie INTEGER,
        data DATE NOT NULL,
        id_aluno INTEGER,
        id_professor INTEGER,
        FOREIGN KEY (id_aluno) REFERENCES aluno (id_aluno)
        FOREIGN KEY (id_professor) REFERENCES professor (id_professor)
        )"""

        self.cursor.execute(query)
        self.conexao.commit()

    def createProfessor(self, nome, sobrenome, email, senha):
        query = "INSERT INTO professor (nome,sobrenome,email,senha) VALUES (?,?,?,?)"
        self.cursor.execute(query, (nome,sobrenome,email,senha))
        self.conexao.commit()
    
    def createAluno(self, nome, sobrenome, id_professor):
        query = "INSERT INTO aluno (nome,sobrenome,id_professor) VALUES (?,?,?)"
        self.cursor.execute(query, (nome, sobrenome, id_professor))
        self.conexao.commit()

    def createExercicio(self, exercicio, repeticao, serie, id_aluno):
        query = "INSERT INTO exercicio (exercicio,repeticao,serie, id_aluno) VALUES (?,?,?,?)"
        self.cursor.execute(query, (exercicio, repeticao, serie, id_aluno))
        self.conexao.commit()

    def findAllAluno(self):
        query = "SELECT * FROM aluno"
        self.cursor.execute(query)
        return self.cursor.fetchall()
   
    def findAllExercicio(self, id_aluno):
        query = "SELECT * FROM exercicio WHERE id_aluno = ?"
        self.cursor.execute(query, id_aluno)
        return self.cursor.fetchall()

    def updateAluno(self, nome, sobrenome, id_aluno):
        query = f"UPDATE aluno SET nome=?,sobrenome=? WHERE id_aluno=?"
        self.cursor.execute(query, (nome, sobrenome, id_aluno))
        self.conexao.commit()  
        
    def updateExercio(self, exercicio, repeticao, serie, id_exercicio):
        query = "UPDATE exercicio SET exercicio=?,repeticao=?,serie=? WHERE id_exercicio=?"
        self.cursor.execute(query, (exercicio, repeticao, serie, id_exercicio))
        self.conexao.commit()

    def removeAluno(self, id_aluno):
        query = "DELETE FROM aluno WHERE id_aluno=?"
        self.cursor.execute(query, (id_aluno,))
        self.conexao.commit()
    
    def removeExercicio(self, id_exercicio):
        query = "DELETE FROM exercicio WHERE id_exercicio=?"
        self.cursor.execute(query, (id_exercicio,))
        self.conexao.commit()

    def fechar_conexao(self):
        return self.conexao.close()

