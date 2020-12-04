from db import cartesngdb
from utils import observer, log


class Model():

    def __init__(self):
        self.logger = log.Logger.Instance()
        self.logger.appdebug('Initialising model')
        self.load_database_instance()
        self.logger.appdebug('Model initialised')

    def load_database_instance(self):
        self.logger.appdebug('Initialising database')
        self.cartesngdb = cartesngdb.CartesNgDb.Instance()
        self.logger.appdebug('Database initialised')

    def select_test(self):
        self.cartesngdb.select_personne()
        observer.Event('update_connect_db', 'Texte sélectionné')
