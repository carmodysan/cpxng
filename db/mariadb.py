#import mariadb
import sys
import json

from utils import singleton, observer


@singleton.Singleton
class MariaDB(object):
    def __init__(self):
        self.load_config()

        # Connect to MariaDB Platform
        try:
            # Refer database
            #self.conn_refer = mariadb.connect(
            #    user=self.db_data['db_connection'][0]['db_user'],
            #    password=self.db_data['db_connection'][0]['db_pwd'],
            #    host=self.db_data['db_connection'][0]['db_host'],
            #    port=int(self.db_data['db_connection'][0]['db_port']),
            #    database=self.db_data['db_connection'][0]['db_database_1'])
            # Cartes database
            #self.conn_cartes = mariadb.connect(
            #    user=self.db_data['db_connection'][0]['db_user'],
            #    password=self.db_data['db_connection'][0]['db_pwd'],
            #    host=self.db_data['db_connection'][0]['db_host'],
            #    port=int(self.db_data['db_connection'][0]['db_port']),
            #    database=self.db_data['db_connection'][0]['db_database_2'])
            self.conn_refer = "test"
            self.conn_cartes = "etest"

            observer.Event('update_connect_db', 'blabla')
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def load_config(self):
        db_file = open('param\\db.json')
        self.db_data = json.load(db_file)
        for i in self.db_data['db_connection']:
            print(i)
        db_file.close()

    def close_connection(self):
        self.conn_refer.close()
        self.conn_cartes.close()

    def __str__(self):
        return 'Database connection object'

    def query_refer(self, query):
        cur = self.conn_refer.cursor()
        cur.execute(query)
        for (id, label, description) in cur:
            print(f"ID: {id}, Label: {label}, Description: {description}")

    def query_cartes(self, query):
        cur = self.conn_cartes.cursor()
        cur.execute(query)
        for (id, label) in cur:
            print(f"ID: {id}, Label: {label}")
