from managers.base_manager import BaseManager
from pymongo import MongoClient
import certifi

class MongoDBManager(BaseManager):

    def __init__(self, db_url, port):
        self.client = MongoClient(db_url, port, tlsCAFile=certifi.where())
        self.db = None

    def set_db(self, db_name):
        self.db = self.client.__getattr__(db_name)
        
    def insert(self, collection, record):
        cl = self.db.__getattr__(collection)
        cl.insert_one(record)

    def find(self, collection, context):
        cl = self.db.__getattr__(collection)
        return cl.find(context)
