from db import cartesngdb


class Model():

    def __init__(self):
        print("Initialize model...")
        self.load_database_instance()
        print("Model initialized")

    def load_database_instance(self):
        self.cartesngdb = cartesngdb.CartesNgDb.Instance()
