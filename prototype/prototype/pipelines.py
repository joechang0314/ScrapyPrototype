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
    # It is first time for me to use scrapy. 
    # This is introduced as I found inserting mongodb in Spider Class parse makes concurrenting not working.
    
    def __init__(self):
        self.settings = get_project_settings()
        self.mongo = MongoDBManager(self.settings['MONGODB_SERVER'], self.settings['MONGODB_PORT'])
        self.mongo.set_db(self.settings['MONGODB_DB'])
        # no need to include in open_spider and closed in close_spider as connection is terminated when process finished.

    def process_item(self, item, spider):
        # todo: check duplication in spider and DropItem
        self.mongo.insert(self.settings['MONGODB_COLLECTION'], dict(item))
        # todo: use findOneAndReplace by url
        logging.info("Artical added to MongoDB database!")

        return item