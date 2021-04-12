import sqlite3
from sqlite3 import Error


class DataBase:
    def __init__(self):
        self.db_file = 'mydatabase.db'
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()
        self.__create_table('''CREATE TABLE collocations (id INTEGER PRIMARY KEY, collocation TEXT NOT NULL)''')

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def __create_table(self, create_table_sql):
        try:
            self.cursor.execute(create_table_sql)
        except Error as e:
            print(e)

    def add_in_collocations(self, collocation):
        self.cursor.execute('INSERT INTO collocations VALUES(NULL, ?)', [collocation])
        self.conn.commit()

    def get_val_collocations(self,):
        self.cursor.execute('''SELECT collocation FROM collocations''')
        return self.cursor.fetchall()

    def __del__(self):
        print('Destructor called, Employee DataBase deleted.')





