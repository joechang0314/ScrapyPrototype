from managers.mongodb_manager import MongoDBManager
from pymongo.database import Database
   

class TestMongodbManager:

    def testSetDB(self):
        mongo = MongoDBManager('test_url', 27017)
        mongo.set_db('Test')
        assert isinstance(mongo.db, Database) == True and mongo.db.name == 'Test'