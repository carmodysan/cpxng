from db import cartesngdb
from utils import observer


class Model():

    def __init__(self):
        print("Initialize model...")
        self.load_database_instance()
        print("Model initialized")

    def load_database_instance(self):
        self.cartesngdb = cartesngdb.CartesNgDb.Instance()

    def select_test(self):
        self.cartesngdb.select_personne()
        observer.Event('update_connect_db', 'Texte sélectionné')
