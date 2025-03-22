import sqlite3

class conexao:

    def __init__(self, db_GymPlanner):
        self.db_GymPlanner = db_GymPlanner
        self.conn = sqlite3.connect(db_GymPlanner)
        self.cursor = self.conn.cursor()

    def get_cursor(self):
        return self.cursor
    
    def commit(self):
        return self.conn.commit()
    
    def close(self):
        return self.conn.close()