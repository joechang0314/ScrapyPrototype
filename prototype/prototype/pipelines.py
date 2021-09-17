# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class PrototypePipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.exceptions import DropItem
import logging
from managers.mongodb_manager import MongoDBManager
from scrapy.utils.project import get_project_settings

class MongoDBPipeline(object):

    def __init__(self):
        self.settings = get_project_settings()
        self.mongo = MongoDBManager(self.settings['MONGODB_SERVER'], self.settings['MONGODB_PORT'])
        self.mongo.set_db(self.settings['MONGODB_DB'])

    def process_item(self, item, spider):

        self.mongo.insert(self.settings['MONGODB_COLLECTION'], dict(item))
        logging.info("Artical added to MongoDB database!")

        return item