from flask import Flask
from flask import request

from managers.mongodb_manager import MongoDBManager
from response import Response
from scrapy.utils.project import get_project_settings
from models.article import Article

import logging
import sys
import traceback

app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        search = request.args.get('search')
        settings = get_project_settings()
        mongo = MongoDBManager(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        mongo.set_db(settings['MONGODB_DB'])
        
        cursor = mongo.find(settings['MONGODB_COLLECTION'], {} if not search else { '$text': { '$search': search } })
        
        response = []
        for article in cursor:
            response.append(Article(article).to_dict())
    except Exception:
        ex_type, ex, tb = sys.exc_info()
        logging.error(str(ex))
        traceback.print_tb(tb)
        return Response.error(str(ex), 400)

    return Response.success(response)