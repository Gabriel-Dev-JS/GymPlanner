import sqlite3

class Repository:
    def __init__(self, db_GymPlanner):
        self.db_GymPlanner = db_GymPlanner
        self.conn = sqlite3.connect(db_GymPlanner)
        self.cursor = self.conn.cursor()
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
        self.conn.commit()
       


    def createTableAluno(self):
        query = """CREATE TABLE IF NOT EXISTS aluno (
        id_aluno INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
        nome TEXT,
        sobrenome TEXT,
        id_professor INTEGER,
        FOREIGN KEY (id_professor) REFERENCES professor (id_professor)
        )"""

        self.cursor.execute(query)
        self.conn.commit()
    
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
        self.conn.commit()

    def createProfessor(self, nome, sobrenome, email, senha):
        query = "INSERT INTO professor (nome,sobrenome,email,senha) VALUES (?,?,?,?)"
        self.cursor.execute(query, (nome,sobrenome,email,senha))
        self.conn.commit()
    
    def createAluno(self, nome, sobrenome, id_professor):
        query = "INSERT INTO aluno (nome,sobrenome,id_professor) VALUES (?,?,?)"
        self.cursor.execute(query, (nome, sobrenome, id_professor))
        self.conn.commit()

    def createExercicio(self, exercicio, repeticao, serie, id_aluno):
        query = "INSERT INTO exercicio (exercicio,repeticao,serie, id_aluno) VALUES (?,?,?,?)"
        self.cursor.execute(query, (exercicio, repeticao, serie, id_aluno))
        self.conn.commit()

    def findAllAluno(self):
        query = "SELECT * FROM aluno"
        self.cursor.execute(query)
        return self.cursor.fetchall()
   
    def findAllExercicio(self):
        query = "SELECT * FROM exercicio"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def updateAluno(self, nome, sobrenome, id_aluno):
        query = f"UPDATE aluno SET nome=?,sobrenome=? WHERE id_aluno=?"
        self.cursor.execute(query, (nome, sobrenome, id_aluno))
        self.conn.commit()  
        
    def updateExercio(self, exercicio, repeticao, serie, id_exercicio):
        query = "UPDATE exercicio SET exercicio=?,repeticao=?,serie=? WHERE id_exercicio=?"
        self.cursor.execute(query, (exercicio, repeticao, serie, id_exercicio))
        self.conn.commit()

    def removeAluno(self, id_aluno):
        query = "DELETE FROM aluno WHERE id_aluno=?"
        self.cursor.execute(query, (id_aluno,))
        self.conn.commit()
    
    def removeExercicio(self, id_exercicio):
        query = "DELETE FROM exercicio WHERE id_exercicio=?"
        self.cursor.execute(query, (id_exercicio,))
        self.conn.commit()

