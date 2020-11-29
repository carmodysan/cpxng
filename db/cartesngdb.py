import sqlite3

from utils import singleton


@singleton.Singleton
class CartesNgDb(object):
    def __init__(self):
        self.load_config()

    def load_config(self):
        self.conn = sqlite3.connect('db/cartes.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        self.insert_personne('10004256598', 'John', 'Rambo', 'M', '99000',
            '29/11/2020')
        self.select_personne()

    def close_connection(self):
        self.conn.close()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Personne (
            id_rpps varchar(255) NOT NULL, prenom_usage varchar(255),
            nom_usage varchar(255), civilite_code varchar(255),
            nationalite_code varchar(255), date_effet varchar(255),
            PRIMARY KEY (id_rpps))''')

    def insert_personne(self, id_rpps, prenom_usage, nom_usage, civilite_code,
        nationalite_code, date_effet):
        param = (id_rpps, prenom_usage, nom_usage, civilite_code,
            nationalite_code, date_effet)
        self.cursor.execute('INSERT INTO Personne VALUES (?,?,?,?,?,?)', param)

    def select_personne(self):
        for row in self.cursor.execute('SELECT * FROM Personne'):
            print(row)
