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
        id_professor INTEGER PRIMARY KEY NOT NULL,
        nome TEXT,
        sobrenome TEXT,
        email TEXT,
        senha TEXT
        )"""

        self.cursor.execute(query)
        self.conexao.commit()
       


    def createTableAluno(self):
        query = """CREATE TABLE IF NOT EXISTS aluno (
        id_aluno INTEGER PRIMARY KEY NOT NULL,
        nome TEXT,
        sobrenome TEXT,
        email TEXT,
        senha TEXT,
        id_professor INTEGER,
        FOREIGN KEY (id_professor) REFERENCES professor (id_professor)
        )"""

        self.cursor.execute(query)
        self.conexao.commit()
    
    def createTableExercicio(self):
        query = """CREATE TABLE IF NOT EXISTS exercicio (
        id_exercicio INTEGER PRIMARY KEY NOT NULL,
        exercicio TEXT,
        repeticao INTEGER,
        serie INTEGER,
        tipo TEXT,
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
    
    def createAluno(self, nome, sobrenome, email, senha, id_professor):
        query = "INSERT INTO aluno (nome,sobrenome,email,senha,id_professor) VALUES (?,?,?,?,?)"
        self.cursor.execute(query, (nome, sobrenome, email, senha, id_professor))
        self.conexao.commit()

    def createExercicio(self, exercicio, repeticao, serie, tipo, id_aluno, id_professor):
        query = "INSERT INTO exercicio (exercicio,repeticao,serie, tipo, id_aluno,id_professor) VALUES (?,?,?,?,?,?)"
        self.cursor.execute(query, (exercicio, repeticao, serie, tipo, id_aluno, id_professor))
        self.conexao.commit()

    def findProfessor(self, email, senha):
        query = "SELECT * FROM professor WHERE email=? and senha=?"
        self.cursor.execute(query,(email, senha))
        return self.cursor.fetchone()
    
    def findProfessorId(self, id_professor):
        query = "SELECT * FROM professor WHERE id_professor=?"
        self.cursor.execute(query,(id_professor,))
        return self.cursor.fetchone()
  
    def findAlunoEmail(self, email):
        query = "SELECT * FROM aluno WHERE email = ?"
        self.cursor.execute(query,(email,))
        return self.cursor.fetchall()

    def findAlunoId(self, id_professor, id_aluno):
        query = """
            SELECT e.id_exercicio, e.id_professor , e.exercicio, e.repeticao , e.serie, e.tipo, a.nome, a.sobrenome, a.id_aluno  
            FROM exercicio e 
            LEFT JOIN  aluno a  ON e.id_aluno = a.id_aluno 
            WHERE e.id_professor=? AND a.id_aluno=?; 
        """
        self.cursor.execute(query,(id_professor, id_aluno))
        return self.cursor.fetchall()
    
    def findAllAluno(self, id_professor):
        query = "SELECT * FROM aluno WHERE id_professor = ?"
        self.cursor.execute(query,(id_professor,))
        return self.cursor.fetchall()
   
    # def findAllExercicio(self, id_aluno, id_professor):
    #     query = "SELECT * FROM exercicio WHERE id_aluno=? and id_professor=?"
    #     self.cursor.execute(query, (id_aluno,id_professor))
    #     return self.cursor.fetchall()

    def updateAluno(self, nome, sobrenome, id_aluno):
        query = "UPDATE aluno SET nome=?,sobrenome=? WHERE id_aluno=?"
        self.cursor.execute(query, (nome, sobrenome, id_aluno))
        self.conexao.commit()  
        
    def updateExercio(self, exercicio, repeticao, serie, id_exercicio, id_aluno, id_professor):
        query = "UPDATE exercicio SET exercicio=?,repeticao=?,serie=? WHERE id_exercicio=? and id_aluno=? and id_professor=?"
        self.cursor.execute(query, (exercicio, repeticao, serie, id_exercicio, id_aluno, id_professor))
        self.conexao.commit()

    def removeAluno(self, id_professor, id_aluno):
        query = "DELETE FROM aluno WHERE id_professor=? and id_aluno=?"
        self.cursor.execute(query, (id_professor, id_aluno))
        self.conexao.commit()
    
    def removeExercicio(self, id_exercicio, id_aluno, id_professor):
        query = "DELETE FROM exercicio WHERE id_exercicio=? and id_aluno=? and id_professor=?"
        self.cursor.execute(query, (id_exercicio,id_aluno, id_professor))
        self.conexao.commit()

    def fechar_conexao(self):
        return self.conexao.close()

