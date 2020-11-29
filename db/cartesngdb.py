import sqlite3

from utils import singleton


@singleton.Singleton
class CartesNgDb(object):
    def __init__(self):
        self.load_config()

    def load_config(self):
        self.conn = sqlite3.connect('cartes.db')

    def close_connection(self):
        self.conn.close()
